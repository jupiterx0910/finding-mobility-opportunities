const DATA_URLS = ["./radar/opportunities.json", "../radar/opportunities.json"];
async function fetchData() {
  let lastError;
  for (const url of DATA_URLS) {
    try {
      const response = await fetch(url, {cache:"no-store"});
      if (response.ok) return response;
      lastError = new Error("数据请求失败：" + response.status + " (" + url + ")");
    } catch (error) { lastError = error; }
  }
  throw lastError || new Error("数据请求失败");
}
const titles = {
  "enterprise-agent-production-governance-evaluation": "企业级 AI Agent 生产治理与评测",
  "lightweight-ai-services-manufacturing-smes": "面向中小制造企业的轻量 AI 服务",
  "embodied-ai-field-deployment-data-integration": "具身智能的现场部署、数据与集成服务",
  "cross-border-compliance-localization-managed-operations": "跨境合规、本地化与托管运营"
};
const summaries = {
  "enterprise-agent-production-governance-evaluation": "围绕企业 Agent 从演示走向生产后的评测、权限、安全、可靠性与治理需求，研究是否存在独立服务商的切入空间。",
  "lightweight-ai-services-manufacturing-smes": "研究中小制造企业能否为具体流程改造、质量/运营效率和可量化结果付费，而不是只购买泛化的 AI 咨询。",
  "embodied-ai-field-deployment-data-integration": "研究机器人进入真实场景后，部署、数据采集、系统集成、维护与安全验证是否形成可持续的服务需求。",
  "cross-border-compliance-localization-managed-operations": "研究出海企业在目标市场合规、本地运营、履约和售后方面是否存在可重复交付的服务缺口。"
};
const sectorFor = slug => slug.includes("cross-border") ? "crossborder" : slug.includes("manufacturing") || slug.includes("embodied") ? "manufacturing" : "ai";
const verdictLabel = value => ({BUY_A_REAL_OPTION:"小额验证",WATCH:"持续观察",START:"开始行动",REJECT:"暂不进入"}[value] || value || "未评级");
const verdictClass = value => value === "START" ? "" : value === "REJECT" ? "orange" : "orange";
let opportunities = [];
let selectedId = null;
const listEl = document.querySelector("#opportunity-list");
const detailEl = document.querySelector("#detail-panel");
const statusEl = document.querySelector("#data-status");
const noticeEl = document.querySelector("#freshness-notice");
const searchEl = document.querySelector("#search");
const sectorEl = document.querySelector("#sector-filter");
const verdictEl = document.querySelector("#verdict-filter");
const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const titleOf = item => titles[item.slug] || item.slug.replaceAll("-", " ");
const summaryOf = item => summaries[item.slug] || "该条目仍是待验证的研究假说，需进一步核查客户付款、复购、利润归属和进入门槛。";
function renderList() {
  const query = searchEl.value.trim().toLowerCase();
  const sector = sectorEl.value;
  const verdict = verdictEl.value;
  const filtered = opportunities.filter(item => {
    const text = [titleOf(item), item.slug, ...(item.payer_hypotheses || []), ...(item.main_power_hypotheses || [])].join(" ").toLowerCase();
    return (!query || text.includes(query)) && (sector === "all" || sectorFor(item.slug) === sector) && (verdict === "all" || item.current_verdict === verdict);
  });
  listEl.innerHTML = filtered.map(item => `
    <article class="opportunity-card ${selectedId === item.id ? "selected" : ""}" data-id="${esc(item.id)}" tabindex="0" role="button" aria-label="查看 ${esc(titleOf(item))}">
      <div class="card-top"><span class="card-id">${esc(item.id)} · ${esc(item.first_seen || "日期未知")}</span><span class="tag ${verdictClass(item.current_verdict)}">${esc(verdictLabel(item.current_verdict))}</span></div>
      <h3>${esc(titleOf(item))}</h3>
      <p class="card-summary">${esc(summaryOf(item))}</p>
      <div class="card-bottom"><span>证据置信度：${esc(item.confidence || "待评估")}</span><strong>查看研究细节 ↗</strong></div>
    </article>`).join("");
  document.querySelector("#empty-state").hidden = filtered.length > 0;
  listEl.querySelectorAll(".opportunity-card").forEach(card => {
    const open = () => selectOpportunity(card.dataset.id);
    card.addEventListener("click", open);
    card.addEventListener("keydown", e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); open(); } });
  });
}
function renderDetail(item) {
  const payers = item.payer_hypotheses || [];
  const powers = item.main_power_hypotheses || [];
  const archetypes = (item.best_fit_archetypes || []).map(x => x.replaceAll("-", " "));
  const sourcePath = item.source_file ? `https://github.com/jupiterx0910/finding-mobility-opportunities/blob/main/${item.source_file}` : "https://github.com/jupiterx0910/finding-mobility-opportunities/tree/main/radar";
  detailEl.innerHTML = `
    <div class="detail-label">OPPORTUNITY FILE / ${esc(item.id)}</div>
    <h3>${esc(titleOf(item))}</h3>
    <p class="detail-summary">${esc(summaryOf(item))}</p>
    <div class="detail-meta"><span>${esc(item.geography || "地区待明确")}</span><span>阶段 ${esc(item.stage || "待评估")}</span><span>${esc(item.status || "状态未知")}</span></div>
    <div class="detail-block"><h4>01 / 潜在付款方 · PAYER HYPOTHESES</h4><ul>${payers.map(x => `<li>${esc(x)}</li>`).join("") || "<li>待研究确认</li>"}</ul></div>
    <div class="detail-block"><h4>02 / 可能的利润捕获点 · POWER HYPOTHESES</h4><ul>${powers.map(x => `<li>${esc(x)}</li>`).join("") || "<li>待研究确认</li>"}</ul></div>
    <div class="detail-block"><h4>03 / 适配的进入者原型</h4><ul>${archetypes.map(x => `<li>${esc(x)}</li>`).join("") || "<li>待研究确认</li>"}</ul></div>
    <div class="detail-block"><h4>04 / 当前证据边界</h4><ul><li>当前判断：${esc(verdictLabel(item.current_verdict))}</li><li>置信度：${esc(item.confidence || "未评估")}</li><li>证据覆盖率：${item.evidence_coverage == null ? "尚未系统计算" : esc(item.evidence_coverage + "%")}</li><li>本页面展示的是研究假说，不代表已验证的商业机会。</li></ul></div>
    <div class="detail-block"><h4>05 / 建议的下一步验证</h4><ul><li>找到 5–10 个目标付款者，访谈其当前工作流程与现有替代方案。</li><li>围绕一个可量化结果提出明确报价，记录拒绝理由与预算来源。</li><li>争取至少 1 个付费试点，并测算交付成本、毛利、回款周期与复购可能。</li><li>提前写下停止条件；若付款意愿或单位经济不成立，及时降级或终止。</li></ul></div>
    <a class="detail-link" href="${esc(sourcePath)}" target="_blank" rel="noreferrer">查看仓库中的研究依据 ↗</a>`;
}
function selectOpportunity(id) {
  const item = opportunities.find(x => x.id === id);
  if (!item) return;
  selectedId = id;
  renderList();
  renderDetail(item);
  if (window.matchMedia("(max-width: 900px)").matches) detailEl.scrollIntoView({behavior:"smooth",block:"start"});
}
async function init() {
  try {
    const response = await fetch(DATA_URL, {cache:"no-store"});
    if (!response.ok) throw new Error("数据请求失败：" + response.status);
    const data = await response.json();
    opportunities = Array.isArray(data.opportunities) ? data.opportunities : [];
    const asOf = data.as_of || "日期未知";
    statusEl.textContent = "研究快照：" + asOf + " · " + opportunities.length + " 条";
    const ageDays = Math.floor((Date.now() - new Date(asOf + "T00:00:00Z").getTime()) / 86400000);
    if (Number.isFinite(ageDays) && ageDays > 30) {
      noticeEl.innerHTML = `<strong>研究快照较旧（${ageDays} 天）</strong><span>当前展示的是 ${esc(asOf)} 的历史数据快照，不代表当前市场状态。自动采集与自动评级流水线尚未启用；请在作出决策前核对最新来源。</span>`;
      statusEl.textContent += " · 历史快照";
    } else {
      noticeEl.innerHTML = `<strong>数据透明提示</strong><span>研究快照日期为 ${esc(asOf)}。研究条目不代表已验证机会；自动更新流水线尚未启用。</span>`;
    }
    renderList();
    if (opportunities.length) selectOpportunity(opportunities[0].id);
    else listEl.innerHTML = '<div class="loading">当前数据集中没有机会条目。</div>';
  } catch (error) {
    statusEl.textContent = "数据读取失败";
    listEl.innerHTML = '<div class="loading">无法载入机会数据。请通过本地 HTTP 服务或 GitHub Pages 打开页面，不要直接以 file:// 方式打开。</div>';
    noticeEl.innerHTML = '<strong>加载失败</strong><span>请检查 radar/opportunities.json 是否存在、是否可访问，以及站点部署路径是否正确。</span>';
  }
}
[searchEl, sectorEl, verdictEl].forEach(el => el.addEventListener("input", renderList));
init();
