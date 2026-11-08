# -*- coding: utf-8 -*-
import json
d=json.load(open('data.json',encoding='utf-8'))
new=[
dict(id="xai-grok-api-watermark-default",date="2026-11-07",co="xAI",cos=["xAI"],types=["政策"],
 title="xAI（SpaceXSI）Grok API 文字輸出 11/7 起預設加隱形浮水印，7 款模型適用",
 url="https://docs.x.ai/developers/advanced-api-usage/watermarking",
 intro="SpaceXSI（原 xAI）開發者文件說明，為符合歐盟 AI 法案，自 2026-11-07 起 grok-4.7、4.6、4.5、4.3 與 grok-4.20 三款變體的 API 文字輸出預設加入隱形浮水印，涵蓋 Responses 與 Chat Completions API、結構化輸出與工具呼叫參數。浮水印透過微調選字實現，不加入任何字元；回應標頭 x-watermark: true 代表已加。團隊管理員可在 Console 逐模型退出（需聲明適用法律例外，並留稽核紀錄），偵測 API 需申請。",
 kw="xAI SpaceXSI Grok API 浮水印 watermark 歐盟 AI 法案 x-watermark grok-4.7 opt-out"),
dict(id="google-antigravity-voice-remote-agents",date="2026-11-06",co="Google",cos=["Google"],types=["產品"],
 title="Google Antigravity 2.29：Gemini Live 語音模式＋雲端遠端代理，關筆電也照跑",
 url="https://9to5google.com/2026/11/06/google-antigravity-remote-agents-voice-mode/",
 intro="9to5Google 11/6 報導，Google 代理式開發平台 Antigravity 2.29（Mac／Windows／Linux）改版：輸入框移到底部、改用 Google Sans 字型；新增由 Gemini Live 驅動的語音模式，可用講的交辦、中途指揮並口頭回覆權限請求，語速 0.75–2 倍可調（官方部落格同日發文，App 與 CLI 皆可用）。最大更新是雲端遠端代理，付費 Google AI Pro／Ultra 用戶可用 GitHub repo 或雲端硬碟資料夾建遠端專案，在獨立雲端 VM 執行，並能用手機監控。",
 kw="Google Antigravity 語音模式 Gemini Live 遠端代理 Remote Agents 雲端 VM AI Pro Ultra 程式代理"),
dict(id="anthropic-components-of-agent-memory",date="2026-11-06",co="Anthropic",cos=["Anthropic"],types=["模型"],
 title="Anthropic 公開代理記憶研究：「做夢」離線整理筆記，Fable 5 用 9 個檔拿 4 枚徽章",
 url="https://www.anthropic.com/research/components-of-agent-memory",
 intro="Anthropic 11/6 發表〈The components of agent memory〉，把代理記憶拆成工作中寫記憶筆記、判斷什麼值得記，以及在閒置時「做夢」（sleep-time compute）回顧逐字稿，修正過時筆記、建立 wiki 式新表示並決定下次預先載入什麼。在 CL-Bench 1.0 中 Opus 5.5、Sonnet 5.5 能把驗證過的規則寫進記憶；玩寶可夢時 Sonnet 3.7 寫了 413 個檔只拿 1 枚徽章，Fable 5 只寫約 10 個檔卻拿到 4 枚。",
 kw="Anthropic 代理記憶 agent memory dreaming 做夢 sleep-time compute CL-Bench Fable 5 Pokémon Claude Managed Agents"),
dict(id="cnbc-anthropic-ipo-valuation-stretch",date="2026-11-06",co="Anthropic",cos=["Anthropic"],types=["投資合作"],
 title="CNBC：科技股重挫後，Anthropic IPO 估值 1.5 兆美元被投資人稱「勉強」，恐降到 1 兆",
 url="https://www.cnbc.com/2026/11/06/investors-brace-for-anthropic-valuation-1point5-trillion-a-stretch.html",
 intro="CNBC 11/6 報導，美國期中選舉民主黨大勝、Nasdaq 週四重挫逾 5%（19 個月最大跌幅）後，部分 Anthropic 投資人下修其 IPO 預期：原本目標約 2 兆美元，如今連 1.5 兆都被形容為「勉強」，有人認為 1 兆至 1.25 兆較可能。Anthropic 預計數週內以代號 ANT 在 Nasdaq 掛牌，今年 5 月私募估值約 9,650 億美元；公司拒絕評論。",
 kw="Anthropic IPO 估值 1.5兆 1兆 Nasdaq ANT 期中選舉 科技股 CNBC"),
dict(id="google-cloud-data-cloud-connectors-gemini",date="2026-11-06",co="Google",cos=["Google"],types=["產品"],
 title="Google Cloud：Gemini for business 加 Data Cloud 連接器，自然語言直查 BigQuery 等企業資料",
 url="https://cloud.google.com/blog/products/data-analytics/query-enterprise-data-in-gemini-with-data-cloud-connectors",
 intro="Google Cloud 11/6 宣布 Gemini for business 推出 Data Cloud 連接器預覽版，業務人員可用自然語言即時查詢 BigQuery、Spanner、AlloyDB、Cloud SQL 與 Looker 中受治理的資料；查詢以使用者本人身分執行，遵守列與欄層級權限，由 Knowledge Catalog 找出相關資料並產生 SQL。結果可直接轉成 Google 文件、Gmail 草稿或 Google 簡報，另可建立附脈絡指示的對話式分析代理。",
 kw="Google Cloud Gemini for business Data Cloud 連接器 BigQuery Looker Spanner AlloyDB 對話式分析 Knowledge Catalog"),
dict(id="aws-bedrock-kimi-k3-1-pro",date="2026-11-06",co="Amazon",cos=["Amazon"],types=["產品"],
 title="AWS Bedrock 上架 Moonshot Kimi K3.1 Pro（Highspeed）：百萬 token 開放權重代理模型",
 url="https://aws.amazon.com/about-aws/whats-new/2026/11/moonshot-ai-kimi-k3-1-pro-on-amazon-bedrock/",
 intro="AWS 11/6 宣布月之暗面（Moonshot AI）Kimi K3.1 Pro 上架 Amazon Bedrock，以 Highspeed 版本提供高輸出速度，主打程式撰寫與文件處理等代理任務。依 Moonshot 說法，這是原生多模態的開放權重代理模型、100 萬 token 脈絡、3 兆參數級，為其最強模型；在 Bedrock 上與專有模型同一安全邊界執行，支援明確提示快取，並透過跨區推論在所有 Bedrock 區域提供。",
 kw="AWS Amazon Bedrock Kimi K3.1 Pro Moonshot 月之暗面 開放權重 百萬token 提示快取 代理"),
dict(id="microsoft-copilot-chat-usage-caps",date="2026-11-06",co="Microsoft",cos=["Microsoft"],types=["價格方案"],
 title="微軟擴大限制免費 Copilot Chat：未買 Copilot 授權的 M365 企業用戶有不公開用量上限",
 url="https://www.computerworld.com/article/4245658/microsoft-extends-undisclosed-usage-restrictions-on-copilot-chat-for-enterprise-users.html",
 intro="Computerworld 11/6 報導，微軟對只有 Microsoft 365 訂閱、未另購 Microsoft 365 Copilot 授權的企業用戶，把合理使用上限擴大到更多 Copilot Chat 功能，但未公開哪些功能、門檻多少；達上限時會提示何時恢復，管理員也無法查看或調整。2,000 席以下組織 11/2 起實施，超過 2,000 席者 11/9 起，被視為推動升級付費 Copilot。",
 kw="Microsoft Copilot Chat 用量上限 fair use Microsoft 365 企業 授權 Copilot license Computerworld"),
dict(id="microsoft-thinkingbox-agent-rl",date="2026-11-06",co="Microsoft",cos=["Microsoft"],types=["模型"],
 title="微軟 ThinkingBox：檢查代理實際留下的紀錄，再拿來強化學習，可靠完成數近 3 倍",
 url="https://commandline.microsoft.com/thinkingbox-part-two-expanded-model-evals-reinforcement-learning-rewards/",
 intro="微軟 11/6 發表 ThinkingBox 第二篇：在隔離環境中讓代理與模擬用戶互動，再核對它實際改動的資料而非只看它說了什麼，評測擴至 18 款模型。範例中 Qwen3.8-27B 20 次有 15 次未經主管核准就改訂房；以同一套終局檢查做 50 步強化學習後，20 次全守規，507 題中「20 次全過」的任務由 38 題增到 107 題，每題可靠完成成本降約 67%。",
 kw="Microsoft ThinkingBox 代理評測 強化學習 RL 政策遵循 Qwen3.8 pass^20 可靠性 模擬用戶"),
dict(id="nvidia-cosmos-3-interactive-world-models",date="2026-11-05",co="NVIDIA",cos=["NVIDIA"],types=["模型"],
 title="NVIDIA Cosmos 3 新增 4 款開放世界模型：自駕多視角＋LiDAR 模擬、機器人動作預測",
 url="https://huggingface.co/blog/nvidia/cosmos-interactive-world-simulation",
 intro="NVIDIA 11/5 在 Hugging Face 發表 Cosmos 3 家族 4 款開放權重檢查點，皆由 Cosmos 3 Nano 後訓練、16B 可訓練參數：Transfer-Auto 生成不同天氣光線的多視角駕駛資料、Sim-Auto 串流同步相機與 LiDAR 觀測、Sim-Transfer 把模擬器控制加文字提示轉成寫實影片、Sim-Bimanual 依機器人動作預測影片。採 OpenMDW 1.1 授權，可商用。",
 kw="NVIDIA Cosmos 3 世界模型 開放權重 自駕 LiDAR 機器人 模擬 Hugging Face OpenMDW"),
dict(id="box-nvidia-nemotron-context-retrieval",date="2026-11-05",co="NVIDIA",cos=["NVIDIA"],types=["投資合作"],
 title="Box 攜手 NVIDIA：Nemotron 驅動的 Box Context Retrieval，宣稱省 9 成 token",
 url="https://blog.box.com/box-partners-nvidia-deliver-trusted-content-layer-enterprise-ai",
 intro="Box 11/5 於 BoxWorks 2026 宣布擴大與 NVIDIA 合作：推出以 Nemotron Retriever 開放模型驅動的 Box Context Retrieval 引擎，可依權限檢索數百萬檔案（含掃描檔、影音），宣稱搜尋準確度（Recall@5）提升 20%、token 用量減 90%、問答快 4 倍，明年初對 Enterprise Advanced 客戶正式提供；Nemotron 3 Ultra 等模型即日進 Box AI，並以 NVIDIA OpenShell 管控代理執行安全。",
 kw="Box NVIDIA Nemotron Context Retrieval BoxWorks OpenShell 企業內容 檢索 RAG 開放權重"),
]
ids={x['id'] for x in d}; urls={x['url'] for x in d}
for n in new:
    assert n['id'] not in ids and n['url'] not in urls, (n['id'], n['url'])
    assert n['date']>='2026-09-01'
d=new+d
json.dump(d,open('data.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(d))
