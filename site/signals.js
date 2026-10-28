(() => {
  const urls = ["./radar/signals.json", "../radar/signals.json"];
  async function fetchSnapshot() {
    let lastError;
    for (const url of urls) {
      try {
        const response = await fetch(url, {cache:"no-store"});
        if (response.ok) return response;
        lastError = new Error("HTTP " + response.status);
      } catch (error) { lastError = error; }
    }
    throw lastError || new Error("Signal snapshot unavailable");
  }
  const list = document.querySelector("#signals-list");
  const status = document.querySelector("#signals-status");
  if (!list || !status) return;
  const esc = value => String(value ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
  const dateLabel = value => {
    if (!value) return "发布时间未知";
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return "发布时间未知";
    return new Intl.DateTimeFormat("zh-CN", {year:"numeric",month:"2-digit",day:"2-digit",timeZone:"UTC"}).format(date);
  };
  const tierLabel = value => ({
    primary_research:"一手研究",
    primary_official:"官方来源",
    primary_company:"企业一手来源",
    secondary_media:"媒体线索",
    unclassified:"来源等级未评估"
  }[value] || value || "来源等级未评估");
  const tagLabel = value => ({
    ai:"AI", enterprise:"企业服务", robotics:"机器人", manufacturing:"先进制造",
    crossborder:"跨境贸易", trade:"贸易", compliance:"合规", automation:"自动化"
  }[value] || value);
  async function load() {
    try {
      const response = await fetchSnapshot();
      const data = await response.json();
      const signals = Array.isArray(data.signals) ? data.signals : [];
      const asOf = data.as_of ? dateLabel(data.as_of) : "尚无成功采集快照";
      status.textContent = asOf + " · " + signals.length + " 条线索";
      if (!signals.length) {
        list.innerHTML = '<div class="loading">尚无已采集的信号。首次自动采集运行后，这里会展示来源、发布时间和原始链接。</div>';
        return;
      }
      list.innerHTML = signals.slice(0, 12).map(item => {
        const tags = (item.topic_tags || []).slice(0, 3).map(tag => '<span class="signal-tag">' + esc(tagLabel(tag)) + '</span>').join("");
        return `<article class="signal-card">
          <div class="signal-card-top"><span class="signal-source">${esc(item.source_name || item.source_id)}</span><span class="signal-tier">${esc(tierLabel(item.reliability_tier))}</span></div>
          <h3><a href="${esc(item.url)}" target="_blank" rel="noreferrer">${esc(item.title)} ↗</a></h3>
          <p>${esc(item.summary || "来源未提供摘要；请打开原始链接核查内容。")}</p>
          <div class="signal-card-bottom"><span>${esc(dateLabel(item.published_at))}</span><span>${tags}</span></div>
          <div class="signal-unverified">UNVERIFIED LEAD · 尚未核实的研究线索</div>
        </article>`;
      }).join("");
    } catch (error) {
      status.textContent = "信号快照暂不可用";
      list.innerHTML = '<div class="loading">暂时无法读取信号快照。可查看仓库中的 radar/collection-report.json 与 GitHub Actions 运行日志。</div>';
    }
  }
  load();
})();
