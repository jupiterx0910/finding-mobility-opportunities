const careerProfiles = {
  "industrial-b2b-sales": {name:"Industrial B2B sales / channel",base:94,wedge:"Start with narrow distribution, sourcing, or managed sales",asset:"relationship → repeat order → supplier/customer data → owned distribution / product",trap:"Do not stay a replaceable broker with no customer ownership."},
  "industrial-field-service": {name:"Industrial field service / maintenance",base:92,wedge:"Sell a paid repair, retrofit, or maintenance outcome",asset:"failure knowledge → SOP → service contract → kit / monitoring data / product",trap:"Do not ignore safety, liability, or founder-heavy delivery."},
  "procurement-supply-chain": {name:"Procurement / supply chain",base:90,wedge:"Sell sourcing, QC, replenishment, or managed procurement",asset:"supplier map → SOP → recurring procurement → data / channel / private-label product",trap:"Do not use employer-confidential supplier or customer data."},
  "ecommerce-operator": {name:"E-commerce operator",base:90,wedge:"Operate a narrow category or merchant outcome before owning inventory",asset:"operations → direct customer list → repeat purchase → brand / product / channel",trap:"Do not confuse rented platform traffic with customer ownership."},
  "domain-operator-ai": {name:"Domain operator + AI",base:88,wedge:"Sell an AI-enabled managed workflow, not generic SaaS",asset:"manual workflow → SOP → agent automation → proprietary evaluation data → software",trap:"Do not build generic AI features before proving a budget owner and ROI."},
  "automation-integrator": {name:"Automation / systems integrator",base:87,wedge:"Sell a retrofit, integration, or monitoring pilot",asset:"project → repeatable module → deployment data → product / recurring monitoring",trap:"Do not let every project remain custom."},
  "cross-border-operator": {name:"Export / cross-border operator",base:86,wedge:"Sell managed localization, compliance, sourcing, or trade operations",asset:"execution → recurring workflow → country/category data → network / fulfillment / brand",trap:"Do not rely on pure information arbitrage that disappears with better tools."},
  "growth-operator": {name:"Performance marketing / growth",base:86,wedge:"Sell a measurable acquisition or conversion outcome",asset:"campaign → playbook → owned audience / CRM → channel / product",trap:"Do not build on paid traffic alone."},
  "quality-engineer": {name:"Quality / manufacturing engineer",base:81,wedge:"Sell supplier quality, testing, or process-improvement outcomes",asset:"failure knowledge → test protocol → data → certification service / product",trap:"Do not underestimate liability or payer distance."},
  "creator": {name:"Creator with direct audience",base:82,wedge:"Sell a narrow paid outcome to the most engaged audience segment",asset:"attention → direct customer list → repeat offer → brand / product / community",trap:"Do not assume audience size equals willingness to pay."},
  "product-manager": {name:"Product manager",base:73,wedge:"Sell a productized vertical service before building software",asset:"problem insight → service → workflow data → vertical tool",trap:"Do not overrate problem framing when payer access is weak."},
  "ai-engineer": {name:"Data / AI engineer",base:72,wedge:"Sell a niche implementation tied to a business outcome",asset:"implementation → reusable agent/eval stack → proprietary data → product",trap:"Do not build before distribution and payer evidence."},
  "software-engineer": {name:"Software engineer",base:70,wedge:"Sell implementation or automation around a painful vertical workflow",asset:"service → repeatable module → software → data / distribution",trap:"Do not mistake low build cost for founder-market fit."},
  "general-admin": {name:"General internal administration",base:48,wedge:"First move closer to transactions, budgets, suppliers, or a repeatable workflow",asset:"execution discipline → specialized service → SOP → recurring account",trap:"Do not quit into an opportunity with no payer access or portable edge."}
};
const form = document.querySelector("#radar-form");
const el = id => document.getElementById(id);
const clamp = (n,min,max) => Math.max(min,Math.min(max,n));
function divergenceState(capital,payment,retention,econ){
  const c = Number(capital.slice(1));
  if(c===5 && payment<2 && retention<2) return "Unwinding";
  if(c>=4 && payment<2 && retention<2) return "Hype Divergence";
  if(c>=3 && payment===2 && retention===2 && econ>=1) return "Formation";
  if(c<=2 && payment===2 && retention===2) return "Underfollowed";
  if(payment===2 && econ===0) return "Subsidy Divergence";
  return "Mixed";
}
function pickVerdict(o){
  const c=Number(o.capital.slice(1));
  if(c===4 && o.payment<2 && o.retention<2) return ["WATCH","watch"];
  if(o.payment===0 || o.payer===0) return ["WATCH","watch"];
  if(o.econ===0 && o.payment===2) return ["REJECT","reject"];
  if(o.score>=82 && o.payer>=2 && o.pilot>=2 && o.payment===2 && o.retention===2) return ["START","start"];
  if(o.score>=68 && o.payer>=1 && o.pilot>=1) return ["BUY A REAL OPTION","option"];
  if(o.score<55) return ["REJECT","reject"];
  return ["WATCH","watch"];
}
function render(e){
  if(e) e.preventDefault();
  const p=careerProfiles[el("career").value];
  const payer=+el("payer").value, supplier=+el("supplier").value, loss=+el("loss").value, pilot=+el("pilot").value;
  const payment=+el("payment").value, retention=+el("retention").value, econ=+el("economics").value;
  const capital=el("capital").value, time=+el("time").value;
  const accessAdjustment=(payer-1.5)*5+(supplier-1.5)*2+(pilot-1.5)*4+(loss-1)*2+(time>=20?3:time<=5?-3:0);
  const score=Math.round(clamp(p.base+accessAdjustment-3,25,98));
  const d=divergenceState(capital,payment,retention,econ);
  const vv=pickVerdict({score:score,payer:payer,pilot:pilot,capital:capital,payment:payment,retention:retention,econ:econ});
  el("readiness").textContent=score+"/100";
  el("payer-score").textContent=["None","Indirect","Some","Weekly"][payer];
  el("divergence").textContent=d;
  el("window").textContent=Number(capital.slice(1))>=3?"Closing faster":"Manageable";
  el("verdict").textContent=vv[0]; el("verdict").className="badge "+vv[1];
  el("why-operator").textContent=p.name+" starts with a "+(score>=85?"strong":score>=70?"usable":"limited")+" transition position.";
  el("operator-detail").textContent="Base archetype readiness "+p.base+"/100, adjusted by payer access, supplier/channel access, available time, affordable loss and paid-pilot feasibility. This is a heuristic, not a probability.";
  el("wedge").textContent=p.wedge;
  const pain=el("pain").value.trim();
  el("wedge-detail").textContent=pain ? "Anchor the offer on this repeated pain: “"+pain.slice(0,180)+"”." : "Name one repeated, expensive pain and one budget owner before expanding the offer.";
  const warningMap={"Hype Divergence":"Capital is running ahead of customer proof.","Formation":"Capital and customer evidence are aligned — competition may accelerate.","Underfollowed":"Customer truth is stronger than investor attention.","Unwinding":"Capital retreat and weak customer proof reinforce each other.","Subsidy Divergence":"Customers pay, but scale worsens contribution economics.","Mixed":"Evidence is mixed. Buy information before conviction."};
  el("warning").textContent=warningMap[d];
  el("warning-detail").textContent=(capital==="C4" && payment<2 && retention<2) ? "Hard guardrail triggered: C4 Euphoric with weak/unverified payment and retention cannot receive START." : "Treat Capital Heat as an environment variable. Payment, retention and contribution economics must independently confirm the thesis.";
  el("pilot-plan").textContent=pilot>=2?"Sell the smallest measurable outcome in 30–60 days.":"Do customer discovery until a paid pilot is reachable.";
  el("pilot-detail").textContent=payer>=2 ? "Use reachable budget owners. Define baseline, deliverable, price, ROI metric and explicit renewal/reorder condition before building more." : "Your first bottleneck is distribution to a payer, not product capability.";
  el("assetization").textContent=p.asset;
  el("dont").textContent=p.trap;
  el("dont-detail").textContent=d==="Hype Divergence" ? "Do not copy venture-backed competitors merely because funding, hiring and media attention are rising." : "Do not make an irreversible commitment until the weakest link has direct evidence.";
}
async function loadRadar(){
  const target=el("opportunity-list");
  try{
    const res=await fetch("../radar/opportunities.json"); if(!res.ok) throw new Error("fetch failed");
    const data=await res.json();
    target.innerHTML=data.opportunities.map(function(o){
      return '<article class="opportunity"><div class="row"><strong>'+o.slug.replaceAll("-"," ")+'</strong><span>'+o.stage+" · "+o.confidence+'</span></div><div class="chips"><span class="chip">'+o.geography+'</span><span class="chip">'+o.current_verdict.replaceAll("_"," ")+'</span><span class="chip">'+o.status+'</span></div></article>';
    }).join("");
  }catch(err){
    target.innerHTML='<p class="fine">Radar JSON is available in the repository, but this viewer blocked relative-file loading. Open through GitHub Pages or a local web server.</p>';
  }
}
el("example-btn").addEventListener("click",function(){
  el("career").value="domain-operator-ai"; el("region").value="china"; el("time").value="10";
  el("industry").value="manufacturing operations"; el("payer").value="2"; el("supplier").value="2";
  el("loss").value="1"; el("pilot").value="2"; el("capital").value="C3"; el("capital-trend").value="Rising";
  el("payment").value="1"; el("retention").value="1"; el("economics").value="1";
  el("pain").value="A weekly manual workflow consumes several staff-hours and creates avoidable rework.";
  el("edge").value="Deep workflow knowledge, access to operators, and the ability to deploy AI-enabled managed services.";
  render();
});
form.addEventListener("submit",render);
loadRadar();
render();