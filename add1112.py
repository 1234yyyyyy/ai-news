# -*- coding: utf-8 -*-
import json
d=json.load(open('data.json',encoding='utf-8'))
new=[
dict(id="openai-chatgpt-plus-veterans-20000",date="2026-11-11",co="OpenAI",cos=["OpenAI"],types=["產品"],
 title="OpenAI 退伍軍人節：已有 2 萬多名退伍與轉職軍人免費領一年 ChatGPT Plus，11 月再辦 5 場培訓",
 url="https://openai.com/index/chatgpt-plus-for-veterans",
 intro="OpenAI 11/11 退伍軍人節發文表示，過去一年已有超過 2 萬名即將退伍的現役軍人與退伍軍人，透過 ID.me 驗證免費領取一年 ChatGPT Plus，用來整理求職、練習面試（含語音模式）、把軍中經歷改寫成民間履歷。OpenAI Academy 與合作夥伴已為近千名軍人社群成員辦了十多場培訓，年底前還有 7 場，包括 11/12 聖路易、11/14 納許維爾、11/17 線上、11/19 達拉斯、11/21 聖安東尼奧。",
 kw="OpenAI ChatGPT Plus 免費 退伍軍人 Veterans Day ID.me OpenAI Academy 求職 履歷 培訓"),
dict(id="openai-control-room-35-seconds",date="2026-11-10",co="OpenAI",cos=["OpenAI"],types=["政策"],
 title="OpenAI 公開 Control Room：研究用模型出問題時，35 秒內切斷所有輸出，服務掛掉也預設封鎖",
 url="https://openai.com/index/control-room/",
 intro="OpenAI 11/10 公開 Control Room，是追蹤並停止研究基礎設施上所有模型工作的中央系統，涵蓋訓練用的代理取樣、評測與資料處理。每個做代理推論的研究工作都要先取得 job_id 並對應核准的安全論證；推論引擎每次產生輸出前都要向 Control Room 確認，研究員或監控模型一喊停，35 秒內該工作就拿不到任何模型輸出（延遲來自授權快取，目標降到零）。系統採「失效即封鎖」，Control Room 本身斷線或被竄改時所有推論請求一律拒絕，已套用到所有前沿模型研究工作。這是 9 月研究代理用 DNS 繞過網路限制事件後的補強。",
 kw="OpenAI Control Room 安全 研究 停止開關 kill switch 監控 推論層 fail-closed DNS 事件 對齊"),
dict(id="google-gemini-decisions-api",date="2026-11-11",co="Google",cos=["Google"],types=["模型"],
 title="Google 推 Gemini Decisions API：新模型 Gemini Decision 1 一次判斷 1,000 題是非選擇，0.25 秒內回答、輸出不收費",
 url="https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/",
 intro="Google DeepMind 11/11 推出 Gemini Decisions API 與新模型 Gemini Decision 1，專做工具選擇、政策檢查、模型路由這類有限選項的判斷：一份文字、圖片、音訊、影片或 PDF 輸入（最多 256K token）可同時問最多 1,000 個是非、多選（2 至 255 個選項）或評分題，模型不逐字生成而是一次算出各選項機率與信心分數，端到端延遲 150 至 250 毫秒。定價每百萬輸入 token 0.10 美元、輸出 0 元，Google 稱整體比 Gemini 3.5 Flash-Lite 便宜近 5 倍；Gemini Notebook 已用它做模型路由，延遲最多降 4 成。已在 Google AI Studio 開放，含免費層。",
 kw="Google Gemini Decisions API Gemini Decision 1 分類 路由 判斷 機率 信心分數 低延遲 AI Studio 定價"),
dict(id="google-gemini-apple-carplay",date="2026-11-11",co="Google",cos=["Google","Apple"],types=["產品"],
 title="Gemini 上 Apple CarPlay：開車時用 Gemini Live 聊天、聽信件摘要、排行程，對話同步回 iPhone",
 url="https://blog.google/innovation-and-ai/products/gemini-app/gemini-on-apple-carplay/",
 intro="Google 11/11 宣布 Gemini App 登上 Apple CarPlay，繼 Android Auto 與內建 Google 的車款之後，iOS 用戶也能在車上螢幕點 Gemini，用 Gemini Live 免手持自然對話：查行事曆、聽每日簡報、摘要未讀 Gmail 並用語音回覆、找附近餐廳，或模擬簡報、讓它扮演難搞的主管練習提案；對話會自動同步到 iPhone 的聊天紀錄。即日起全球所有支援 Gemini Live 語言的 iOS 用戶陸續可用，需更新 App 並先在手機用過一次 Gemini Live；每日簡報等個人化功能未滿 18 歲、歐洲經濟區與奈及利亞不提供。",
 kw="Google Gemini CarPlay Apple iPhone 車用 Gemini Live 語音 開車 Gmail 行事曆 每日簡報"),
dict(id="nvidia-openshell-cncf-kubecon",date="2026-11-10",co="NVIDIA",cos=["NVIDIA","Google"],types=["產品"],
 title="NVIDIA 在 KubeCon 把 AI 代理安全執行環境 OpenShell 捐給 CNCF，並開源 3 款 Kubernetes GPU 工具",
 url="https://blogs.nvidia.com/blog/open-source-openshell-infrastructure/",
 intro="NVIDIA 11/10 在 KubeCon 宣布把開源代理安全執行環境 OpenShell 捐給 Linux 基金會旗下的 CNCF，成為沙盒專案；它能對代理的工具使用、推論存取與執行套用確定性政策，上線不到一年已有數百家組織採用。NVIDIA 也參與 Google 主導的 Agent Substrate（在 Kubernetes 上大規模跑長時間代理），雙方將整合兩者。另開源 DSX AI Factory 平台的 NVIDIA Kubernetes Engine、Kubernetes Recipes（公開預覽）與 Snapshot：Snapshot 可在幾秒內還原推論副本，Crusoe 實測讓 GLM-5.3 就緒時間從約 8 分鐘縮到 31 秒。",
 kw="NVIDIA OpenShell CNCF KubeCon Kubernetes 開源 代理安全 Agent Substrate Google NVKE Snapshot DSX AI 工廠"),
dict(id="nvidia-elevenlabs-voice-agents-expand",date="2026-11-11",co="NVIDIA",cos=["NVIDIA","其他"],types=["投資合作"],
 title="ElevenLabs 與 NVIDIA 擴大合作：Nemotron 進 ElevenAgents，加 15MW Vera Rubin 算力，替波蘭國家醫療跑語音代理",
 url="https://elevenlabs.io/blog/nvidia",
 intro="ElevenLabs 11/11 在紐約宣布與 NVIDIA 擴大合作：NVIDIA Nemotron 3.5 Super VL 加入對話代理平台 ElevenAgents，在客服任務基準上完成率領先、成本比其他主流開放模型低 70%；ElevenLabs 也將在既有 Blackwell Ultra 系統之外，自建 15MW 的 Vera Rubin 算力。雙方首個主權部署是波蘭國家電子醫療平台的中央掛號系統，用語音代理打電話提醒只有市話的病患並協助改約，在本地以 NVIDIA 機密運算執行，資料不出政府機房；之後也要把語音 AI 帶到機器人與車輛等邊緣裝置。NVIDIA 2025 年已投資 ElevenLabs。",
 kw="NVIDIA ElevenLabs 語音代理 ElevenAgents Nemotron 3.5 Super VL Vera Rubin Blackwell Ultra 波蘭 主權 AI 醫療 黃仁勳"),
dict(id="microsoft-copilot-claude-fable-5-2",date="2026-11-11",co="Microsoft",cos=["Microsoft","Anthropic"],types=["產品"],
 title="微軟 Copilot 上架 Claude Fable 5.2：Copilot Cowork 與 Copilot Studio 陸續開放，可用公司檔案與會議當背景",
 url="https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/available-today-anthropic-claude-fable-5-2-in-microsoft-copilot/4571829",
 intro="微軟 11/11 宣布 Anthropic 兩天前發表的 Claude Fable 5.2 開始在 Copilot Cowork 與 Copilot Studio 推出，讓企業能依工作挑選前沿模型。Copilot 的 Work IQ 會在既有權限內，用組織的檔案、會議、聊天與業務資料替 Fable 5.2 提供背景，回答附可追溯的來源。管理員可在 Microsoft 365 系統管理中心控管存取與開放範圍，實際上線時間依地區與組織而異。",
 kw="Microsoft 微軟 Copilot Cowork Copilot Studio Anthropic Claude Fable 5.2 Work IQ Microsoft 365 企業 模型選擇"),
dict(id="meta-muse-models-google-cloud",date="2026-11-10",co="Meta",cos=["Meta","Google"],types=["投資合作"],
 title="Meta Muse 模型上 Google Cloud：Muse Ember、Spark 1.3、Wonder 進 Model Garden，Pichai 公開歡迎",
 url="https://www.fortuneindia.com/technology/meta-takes-its-ai-models-to-google-cloud-adds-three-models-to-model-garden/169681",
 intro="Fortune India 報導，Meta 執行長祖克柏在 X 宣布 Muse Ember、Muse Spark 1.3 與 Muse Wonder 三款模型已在 Google Cloud 上架，Google 執行長 Pichai 隨即回文歡迎它們加入 Model Garden。企業可透過託管 API 直接使用，不必自己架模型。報導指出，Google 與 Meta 雖在模型上互為對手，雲端平台仍願意提供他家模型，Meta 則多了一條接觸企業開發者的管道；Google Cloud 10 月也已上架 OpenAI 的 GPT-6 系列。",
 kw="Meta Muse Ember Muse Spark 1.3 Muse Wonder Google Cloud Model Garden Vertex 祖克柏 Pichai 雲端 模型上架"),
dict(id="alibaba-qwen4-max-preview",date="2026-11-11",co="阿里巴巴 Qwen",cos=["中國大廠"],types=["模型"],
 title="阿里巴巴開放 Qwen4-Max 預覽：新一代旗艦模型，支援圖片與影片輸入、百萬 token 上下文",
 url="https://technode.com/2026/11/11/alibaba-opens-qwen4-max-preview-with-a-million-token-context-window/",
 intro="TechNode 11/11 報導，阿里巴巴週三開放新一代 Qwen 家族旗艦 Qwen4-Max 的預覽版，支援圖片與影片輸入，上下文最長 100 萬 token。開發者可透過阿里的 Token Plan 訂閱使用，Qwen App、Qoder、QwenWork 與 QwenStudio 也已能搶先試用。",
 kw="阿里巴巴 Alibaba Qwen Qwen4-Max 通義千問 旗艦模型 預覽 百萬 token 多模態 影片 Token Plan Qoder"),
dict(id="aws-emulator-built-by-agents",date="2026-11-11",co="Amazon",cos=["Amazon"],types=["產品"],
 title="AWS 推本機模擬器 AWS Emulator：程式碼 100% 由數千個 AI 代理寫成、沒有人審，CC0 開源",
 url="https://www.aboutamazon.com/news/aws/how-autonomous-ai-agents-built-aws-emulator",
 intro="AWS 11/11 推出 AWS Emulator，可在自己電腦上模擬 AWS 服務來開發與測試應用，每一行程式碼都由自主 AI 代理寫成，團隊沒寫也沒審過。資深首席工程師 Matthew Goldberg 說明，代理分三組：一組依 AWS API 模型寫測試並先對真實 AWS 驗證（已有數萬個），一組重放測試找出差異並開 issue，一組各自修一個 issue，再經過編譯、程式規範、安全與回歸檢查的關卡才合併，每天修掉數千個問題。原始碼與測試以 CC0 公眾授權放上 GitHub，連代理做過的所有 issue 都看得到。",
 kw="Amazon AWS Emulator 本機模擬器 AI 代理 自主開發 Kiro CC0 開源 GitHub 測試 多代理"),
]
ids={x['id'] for x in d}; urls={x['url'] for x in d}
for n in new:
    assert n['id'] not in ids and n['url'] not in urls, (n['id'], n['url'])
    assert n['date']>='2026-09-01'
d=sorted(new+d,key=lambda x:x['date'],reverse=True)
json.dump(d,open('data.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(d), 'added', len(new))
