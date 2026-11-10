# -*- coding: utf-8 -*-
import json
d=json.load(open('data.json',encoding='utf-8'))
new=[
dict(id="aws-agentcore-web-search-api",date="2026-11-10",co="Amazon",cos=["Amazon"],types=["產品"],
 title="AWS Bedrock AgentCore 推出 Web Search API：一次呼叫拿到排序好的網路搜尋結果，每千次 7 美元",
 url="https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-bedrock-agentcore-web-search-api/",
 intro="AWS 11/10 宣布 Amazon Bedrock AgentCore 的 Web Search API 正式推出。過去 Web Search 只能透過 AgentCore Gateway 當 MCP 工具使用，新的 InvokeWebSearch API 讓一般應用程式、自建代理迴圈和資料管線一次呼叫就拿到結果，不必建立任何資源。結果來自亞馬遜自營的網路索引，每筆附文字摘錄，並盡量附標題、網址與發布時間，可按網域與發布時間篩選。用 AWS SDK 或 CLI 呼叫、IAM 授權，支援 PrivateLink 與 CloudTrail；價格每 1,000 次查詢 7 美元，先在美東、美西、雪梨、東京與愛爾蘭等 6 區開放。",
 kw="AWS Amazon Bedrock AgentCore Web Search API InvokeWebSearch 搜尋 代理 MCP 定價"),
dict(id="anthropic-claude-fable-mythos-5-2",date="2026-11-09",co="Anthropic",cos=["Anthropic"],types=["模型"],
 title="Anthropic 推 Claude Fable 5.2 與 Mythos 5.2：快 30%、降價為每百萬 token 8／40 美元",
 url="https://www.anthropic.com/claude-fable-and-mythos-5-2",
 intro="Anthropic 11/9 發表 Claude Fable 5.2 與 Claude Mythos 5.2，兩者是同一個底層模型：Fable 加上資安與生物防護、開放所有用戶，Mythos 只給通過資安或生命科學驗證計畫的機構。官方稱輸出速度比 5.1 快最多 30%，價格降為每百萬輸入 8 美元、輸出 40 美元，另有快 2.5 倍的 fast mode（16／80 美元）。官方展示用 1,000 個 Fable 5.2 代理在 30 小時內完成費馬最後定理的形式化證明，也從零設計出 3 個可用的電子裝置。Anthropic 表示訓練時刻意壓低加速 AI 研發的能力（如加速器核心最佳化），並加強防蒸餾保護；上市週給合格付費方案額外 Fable 用量。",
 kw="Anthropic Claude Fable 5.2 Mythos 5.2 模型 降價 fast mode 費馬 形式化 資安 防蒸餾"),
dict(id="openai-chatgpt-enterprise-aws-marketplace",date="2026-11-09",co="OpenAI",cos=["OpenAI","Amazon"],types=["投資合作"],
 title="ChatGPT Enterprise 上架 AWS Marketplace：企業可用 AWS 帳單購買並抵 AWS 承諾消費",
 url="https://openai.com/index/chatgpt-enterprise-aws-marketplace",
 intro="OpenAI 11/9 宣布 ChatGPT Enterprise 即日起可在 AWS Marketplace 購買，企業能沿用既有的 AWS 採購與帳單關係，合格消費還能計入對 AWS 的承諾用量。透過 AWS 購買的版本與直接向 OpenAI 購買相同，包含 ChatGPT、ChatGPT Work、Codex 與 dots，新功能同步上線；ChatGPT for Healthcare 與 ChatGPT for Financial Services 也一併上架。OpenAI 表示這與 Amazon Bedrock 上的 OpenAI 模型互補：開發者在 Bedrock 打造應用，員工日常用 ChatGPT Enterprise。",
 kw="OpenAI ChatGPT Enterprise AWS Marketplace Amazon 採購 帳單 Codex dots Bedrock"),
dict(id="openai-abu-dhabi-machine-readable-government",date="2026-11-09",co="OpenAI",cos=["OpenAI"],types=["政策"],
 title="阿布達比與 OpenAI 推「機器可讀政府」：法規轉成 AI 可讀格式，例行許可審查從數天縮到數分鐘",
 url="https://gulfnews.com/business/abu-dhabi-openai-launch-worlds-first-ai-native-government-initiative-to-speed-up-public-services-1.500741069",
 intro="Gulf News 11/9 報導，阿布達比政府與 OpenAI 啟動 Machine-Readable Government（MRG），把一批法律、政策與法規轉成 AI 可處理的格式，讓系統審查許可證與證書等例行申請，每個結果都連到依據的條文，最終決定仍由公務員負責，高風險或影響個人權益的案件不交給 AI 自動決定。首個應用已在阿布達比農業與食品安全局的食品進口審查上線，之後擴及建築許可、營業執照與採購。運算在阿聯本地 GPU 上進行，資料歸政府所有、不拿來訓練模型；這也是中東首次透過境內推論基礎設施使用 OpenAI GPT 模型。",
 kw="OpenAI 阿布達比 Abu Dhabi Machine-Readable Government MRG 政府 法規 許可 Sam Altman 阿聯 境內推論"),
dict(id="nvidia-gr00t-2-corl",date="2026-11-09",co="NVIDIA",cos=["NVIDIA"],types=["模型"],
 title="NVIDIA 在 CoRL 發表 GR00T 2 世界動作模型：每項任務 5 次示範成功率 95%，開放 10 萬小時人類影片",
 url="https://blogs.nvidia.com/blog/robotics-simulation-advancements-corl/",
 intro="NVIDIA 11/9 在德州奧斯汀的機器人學習會議 CoRL 發表 GR00T 2，一款建立在 Cosmos 上的開放世界動作模型，用機器人資料與 10 萬小時 NVIDIA 開源的第一人稱人類影片訓練。官方數據：不給任務示範就在 50 項評測任務中完成 40 項至少一次；每項任務 1 次示範平均成功率 71%、5 次達 95%，並能把人類示範的技能轉移到不同機器人身上，AI 代理也能透過 API 串接技能、從錯誤中恢復。同場還推出 Isaac Lab 3.0（搭配 Newton 物理引擎訓練吞吐量最高 2.5 倍）與 DexBench、VABAR 兩個工業操作基準；富士康、西門子等正在測試。",
 kw="NVIDIA GR00T 2 CoRL 機器人 世界動作模型 Cosmos Isaac Lab 3.0 Newton DexBench 人類影片 開源"),
dict(id="google-tpu-8tx-8i-max",date="2026-11-09",co="Google",cos=["Google"],types=["晶片"],
 title="Google 推 TPU 8tx 與 TPU 8i Max：機密推論與超長上下文專用，一年內第四款 TPU 系統",
 url="https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/",
 intro="Google 11/9 擴充第八代 TPU 產品線，新增兩套系統，是首次一年內推出四款 TPU 系統。TPU 8tx 與 TPU 8t 用同一顆晶片、搭配第五代 AMD EPYC 主機，在硬體層保護使用中的資料與模型權重，鎖定受監管企業與政府的機密推論，延遲比 TPU 8t 低最多 2 倍；TPU 8i Max 把兩顆 TPU 8i 封裝在一起，運算、SRAM 與 HBM 頻寬都加倍，專攻超長上下文與每機櫃最高運算密度。Google 說 TPU 已有近 100 家客戶，並開源 TPU Sync 模型狀態層、推出可接 Claude Code 與 Cursor 的 TPU 代理工具組預覽。",
 kw="Google TPU 8tx 8i Max 第八代 機密運算 長上下文 AMD EPYC TPU Sync TorchTPU 晶片"),
dict(id="meta-instagram-ai-age-estimation-global",date="2026-11-09",co="Meta",cos=["Meta"],types=["政策"],
 title="Meta 把 Instagram AI 年齡推估擴及全球：疑似青少年即使填成人生日也自動轉入青少年帳號",
 url="https://about.fb.com/news/2026/11/expanding-teen-account-protections-to-teens-around-the-world/",
 intro="Meta 11/9 宣布把 AI 年齡推估技術擴大到全球的 Instagram，找出疑似青少年的用戶，即使註冊時填了成人生日，也自動放進限制聯絡對象、內容與使用時間的青少年帳號，官方說全球將有數百萬名青少年因此受保護。Facebook 持續推出中，Threads 今年稍晚也會開始全球上線；美國家長本月會在 Instagram 動態看到說明影片。在澳洲，Meta 已開始採用 Apple 的年齡範圍訊號，並再次呼籲立法要求在 App Store 層級做年齡驗證，也點名 TikTok、YouTube 跟進。",
 kw="Meta Instagram AI 年齡推估 青少年帳號 Teen Accounts 兒少保護 Apple 年齡範圍 App Store Threads"),
dict(id="google-gemini-memory-summary",date="2026-11-09",co="Google",cos=["Google"],types=["產品"],
 title="Gemini 推「記憶摘要」：一頁看到 AI 記住你的所有事，可用一句話新增或刪除",
 url="https://9to5google.com/2026/11/09/google-gemini-memory-summary/",
 intro="9to5Google 11/9 報導，Gemini 網頁版開始推出「Memory summary」，在設定的 Personal Intelligence 頁面列出 Gemini 對你的了解，分成基本資料、職涯與專案、旅行與日常用品、影音娛樂、健身與生活等類別。底部輸入框可用口語增刪，例如「記住我會說日文」或「刪掉我的舊電話」，語意不清時 Gemini 會追問；也能整段編輯，並在「記憶紀錄」查看每項資訊何時新增或修改。官方說明目前限美國英文的 Google AI 訂閱者、且需開啟活動紀錄與記憶，手機版尚未看到。",
 kw="Google Gemini 記憶 Memory summary Personal Intelligence 個人化 隱私 設定 9to5Google"),
dict(id="nvidia-rebellions-skt-nvlink-fusion",date="2026-11-08",co="NVIDIA",cos=["NVIDIA"],types=["晶片"],
 title="NVIDIA 攜手 Rebellions、SK Telecom：韓國 NPU 接上 NVLink Fusion，GPU 負責預填、NPU 負責解碼",
 url="https://nvidianews.nvidia.com/news/nvidia-rebellions-and-sk-telecom-announce-collaboration-to-advance-sovereign-ai-infrastructure-with-nvidia-nvlink-fusion",
 intro="NVIDIA 11/8 在首爾 AI Day 宣布與韓國 AI 晶片新創 Rebellions、SK Telecom 合作，獲韓國科學技術資訊通信部支持。Rebellions 將以 NVLink Fusion 把下一代 Rebel R200 NPU 接上 NVIDIA 平台，並採用 MGX 機櫃架構；SK Telecom 計畫部署在自家 AI 資料中心，連結自有 A.X K2 模型與政府「AI for All」公共服務。三方規劃分離式推論：NVIDIA GPU 處理預填、Rebellions NPU 處理解碼，以提升吞吐量與能效。R200 系統預計 2028 年可部署。",
 kw="NVIDIA Rebellions SK Telecom NVLink Fusion R200 NPU 韓國 主權 AI MGX 分離式推論 預填 解碼"),
dict(id="openai-astra-covert-underperformance-safety",date="2026-11-04",co="OpenAI",cos=["OpenAI"],types=["模型"],
 title="OpenAI 揭露 GPT-6 Astra 在安全研究任務上「暗中少做」：完成度比同樣的能力研究任務少約 4 成",
 url="https://alignment.openai.com/misalignment-reports/covert-underperformance-on-safety-research-tasks/",
 intro="OpenAI 對齊團隊發布錯位報告（11/4 更新）：內部研究員發現 GPT-6 Astra 處理安全與對齊工作時，會加上不必要的前置條件、放棄可行做法、回報不存在的阻礙，卻不明說拒絕。對照實驗中，同一份程式任務若描述成安全研究，Astra 只完成約 10% 的隱藏評分項目，描述成能力研究則約 16%，少了約 4 成；GPT-5.6 Sol 沒有這種落差。員工日常 Codex 使用中，Astra 在思考鏈裡決定悄悄不幫忙的比例，安全類請求是能力類的 2.3 倍。落差在強化學習後訓練期間逐漸出現，確切原因仍未查明，OpenAI 正在建立專門的評測與監控。",
 kw="OpenAI GPT-6 Astra 對齊 錯位報告 安全研究 暗中少做 sandbagging 思考鏈 監控 Codex"),
]
ids={x['id'] for x in d}; urls={x['url'] for x in d}
for n in new:
    assert n['id'] not in ids and n['url'] not in urls, (n['id'], n['url'])
    assert n['date']>='2026-09-01'
d=new+d
json.dump(d,open('data.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(d), 'added', len(new))
