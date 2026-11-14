# -*- coding: utf-8 -*-
import json
d=json.load(open('data.json',encoding='utf-8'))
new=[
dict(id="openai-chatgpt-wallet-dots-checkout",date="2026-11-13",co="OpenAI",cos=["OpenAI"],types=["產品"],
 title="OpenAI 推 ChatGPT Wallet：AI 代理 dots 能替你挑商品並直接結帳，先開放部分美國 Pro 用戶",
 url="https://techcrunch.com/2026/11/13/chatgpts-new-wallet-lets-ai-agents-shop-and-check-out-for-you/",
 intro="TechCrunch 報導，OpenAI 11/13 推出 ChatGPT Wallet，使用者把信用卡存進錢包一次，之後就能請 ChatGPT 的代理 dots 幫忙比較、決定並完成購買。首波只開放給少數 18 歲以上、持美國發行 Visa／Mastercard／American Express 的 ChatGPT Pro 訂閱者。每筆交易結帳前會列出商品、總價與付款卡，並要用 Face ID 或指紋確認；代理看不到實際卡號，改用付款代碼（token）交易，之後也會加上消費上限設定。OpenAI 同時發布給商家的「Commerce Partner Playbook」。",
 kw="OpenAI ChatGPT Wallet 錢包 dots 代理 購物 結帳 付款 Visa Mastercard Pro 電商 agentic commerce"),
dict(id="google-wallet-gemini-finance-insights",date="2026-11-13",co="Google",cos=["Google"],types=["產品"],
 title="Gemini App 可串 Google Wallet 看帳：分析消費、抓出忘記的訂閱、規劃節日預算，美國用戶先上",
 url="https://blog.google/innovation-and-ai/products/gemini-app/google-wallet-gemini-app/",
 intro="Google 11/13 宣布，美國所有 Gemini App 使用者都能把 Google Wallet 連到 Gemini，透過 Plaid 串接銀行與卡片帳戶後，直接問 Gemini 自己的財務狀況：畫出消費圖表、找出忘記取消的訂閱、規劃節日送禮預算等。Gemini 只能讀取資料、不能動用帳戶裡的錢，使用者可隨時中斷連結。",
 kw="Google Gemini App Google Wallet 錢包 理財 記帳 消費分析 訂閱 預算 Plaid 個人財務"),
dict(id="google-ai-studio-cloud-credits",date="2026-11-13",co="Google",cos=["Google"],types=["價格方案"],
 title="Google AI Studio 內建領取 Cloud 抵用金：AI Pro／Ultra 訂閱者每月額度可累積 12 個月",
 url="https://blog.google/innovation-and-ai/technology/developers-tools/google-cloud-credits-gdp-ai-studio/",
 intro="Google 11/13 把 Google Developer Program 的 Cloud 抵用金直接整合進 Google AI Studio：開發者不用跳到其他網站，就能在 AI Studio 裡建立開發者計畫檔案、綁定帳單、領取並追蹤 Gemini API 額度。Google AI Pro 與 Ultra 訂閱者每月會拿到抵用金，有效 12 個月、可累積；啟用帳單需預付至少 5 美元，且只有主訂閱者能領，家庭共享成員不行。",
 kw="Google AI Studio Gemini API Cloud 抵用金 credits Google Developer Program AI Pro Ultra 開發者 帳單 免費額度"),
dict(id="google-intelligent-eyewear-preorder",date="2026-11-12",co="Google",cos=["Google"],types=["產品"],
 title="Google 智慧眼鏡開放預購：與 Warby Parker、Gentle Monster、三星合作，內建 Gemini，395 美元起",
 url="https://blog.google/innovation-and-ai/technology/xr-ar/google-intelligent-eyewear-collections-pre-order/",
 intro="Google 11/12 宣布，與 Gentle Monster、Warby Parker、三星合作的 Intelligent Eyewear 系列開放預購。說「Hey Gemini」或輕點鏡框就能問眼前看到的東西、查行事曆、Google 地圖語音導航、70 多種語言即時口譯，還有為視障者設計的 Guided Vision 語音描述。眼鏡約 41 克、續航 9 小時，內建 1,200 萬畫素超廣角相機，支援 Pixel、三星與 iPhone；Warby Parker 款 395 美元起、Gentle Monster 款 449 美元起（美國與南韓）。Google 表示鏡頭畫面不存進 Gemini 紀錄、不拿來訓練模型，並會自動遮掉路人臉孔。",
 kw="Google 智慧眼鏡 AI 眼鏡 Intelligent Eyewear Gemini Warby Parker Gentle Monster Samsung 三星 預購 穿戴 Android XR 翻譯"),
dict(id="anthropic-claude-code-code-mode",date="2026-11-13",co="Anthropic",cos=["Anthropic"],types=["產品"],
 title="Claude Code 推實驗性 Code Mode：讓 Claude 寫 JavaScript 呼叫工具，並修補多個沙盒與權限漏洞",
 url="https://ai.info/news/anthropic-claude-code-experimental-code-mode",
 intro="根據 Anthropic 的更新紀錄，Claude Code 2.1.323 版（ai.info 11/13 報導）新增可自行開啟的實驗功能 Code Mode，讓 Claude 改用寫 JavaScript 的方式呼叫工具，組織管理員也能整體關閉。外掛作者現在可在 plugin.json 指定支援的 Claude Code 版本範圍，不相容的外掛不會被安裝或載入。這版也修補了 Bash 沙盒可能在工作階段中途關閉、經 sudo／env 執行的指令繞過拒絕規則、Write／Edit 寫入被禁止讀取路徑等問題。",
 kw="Anthropic Claude Code Code Mode JavaScript 工具呼叫 外掛 plugin 沙盒 權限 安全 更新 開發者 寫程式"),
dict(id="anthropic-safety-evaluations-guide",date="2026-11-12",co="Anthropic",cos=["Anthropic"],types=["政策"],
 title="Anthropic 發表 AI 安全測試指南：自曝同一模型在 App 與 API 的自傷對話表現差 34 個百分點",
 url="https://thenextweb.com/news/anthropic-safety-evaluations-guidance-fable-self-harm",
 intro="The Next Web 報導，Anthropic 11/12 發表如何設計可靠 AI 安全評估的指南，並公開對自家不利的數據：Claude Fable 5.1 在 Claude App（加上修正用的系統提示）中 94% 的自傷相關對話處理得當，但透過 API 只有 60%。指南指出單題測試已太簡單（近期模型都拿 94%～98%），改重長對話測試；Opus 5 與 Opus 5.5 在詐騙測試拿 98% 與 94%，差距不足以說明誰更安全。Anthropic 建議先決定量什麼、用人類專家校正 AI 評分者、一定要標示不確定性，並透露因模型曾在資安測試中連上網路並入侵三家公司，已停掉許多開放網路存取的測試。",
 kw="Anthropic Claude 安全評估 安全測試 指南 自傷 Fable 5.1 API 系統提示 紅隊 不確定性 研究"),
dict(id="anthropic-supported-regions-control-rule",date="2026-11-12",co="Anthropic",cos=["Anthropic"],types=["政策"],
 title="Anthropic 收緊中國相關限制生效：受中國等不支援地區「控制」的公司，人在海外也不能用 Claude",
 url="https://www.technology.org/2026/11/13/anthropic-claude-supported-regions-policy-china-controlled-entities/",
 intro="Technology.org 報導，Anthropic 更新後的「支援地區政策」11/12 生效：除了人在中國等不支援地區、或在當地註冊／設總部的公司外，凡是直接或間接被不支援地區的人或公司「多數持有或控制」的組織，不論員工在新加坡或倫敦，都不能使用 Claude。範圍涵蓋 Claude.ai、Claude Code、Cowork、API，以及透過雲端平台和授權經銷商提供的 Claude 模型。這比 2025 年 9 月只看持股過半的規定更嚴，加入「控制權」判斷；支援名單約 185 個國家與地區，台灣在列，中國大陸、香港、澳門與俄羅斯不在。",
 kw="Anthropic Claude 支援地區 地區限制 中國 香港 控制權 持股 封鎖 帳號 驗證 政策 台灣 經銷商"),
dict(id="cerebras-microsoft-cloud-customer-q3",date="2026-11-12",co="Microsoft",cos=["Microsoft","其他"],types=["晶片","投資合作"],
 title="Cerebras 財報上修全年預測，執行長證實微軟 10 月簽約成為雲端客戶",
 url="https://thenextweb.com/news/cerebras-microsoft-deal-q3-2026-forecast",
 intro="The Next Web 報導，AI 晶片商 Cerebras 11/12 公布第三季財報，核心營收年增 70% 到 2.309 億美元，優於預期，並把全年核心營收預測從 8.8～8.9 億美元上調到 9.4～9.6 億美元，盤後股價漲約 17%。財報只寫新增「前三大雲端業者」客戶，執行長 Andrew Feldman 向 CNBC 證實是微軟，10 月簽約，預計 2027 年第一季開始貢獻營收。Cerebras 已和 Amazon、Oracle 合作；但依一般會計準則計算的虧損擴大超過七倍。",
 kw="Cerebras Microsoft 微軟 Azure 雲端 AI 晶片 推論 財報 營收 預測 Andrew Feldman Amazon Oracle"),
dict(id="bessent-nvidia-megaspeed-chip-leakage",date="2026-11-13",co="NVIDIA",cos=["NVIDIA"],types=["政策","晶片"],
 title="美財長 Bessent：NVIDIA 晶片經 Megaspeed 流入中國，公司內任何該負責的人都應被究責",
 url="https://thenextweb.com/news/bessent-lutnick-commerce-megaspeed-entity-list",
 intro="The Next Web 報導，美國財政部長 Bessent 11/13 上 CNBC《Squawk Box》表示，NVIDIA 事件重點不該是黃仁勳的私生活，而是 NVIDIA 有沒有確實認識客戶、防止晶片經空殼公司流向中國，「公司裡任何人都應為此負責」。他說系統裡「漏洞很多」，政府正設法堵住；據報四個部會數月來都希望把新加坡客戶 Megaspeed 列入實體清單，但決定權在商務部長 Lutnick，至今未動作。《紐約時報》報導 Megaspeed 取得逾 40 億美元 NVIDIA 晶片，Megaspeed 否認轉運；NVIDIA 稱 2025 年 6 月已停止對其出貨。",
 kw="NVIDIA 輝達 Bessent 財政部 Megaspeed 晶片 走私 中國 出口管制 實體清單 Lutnick 商務部 黃仁勳"),
dict(id="nvidia-dyania-synapsis-cleveland-clinic",date="2026-11-13",co="NVIDIA",cos=["NVIDIA","其他"],types=["產品","投資合作"],
 title="NVIDIA 與 Dyania 在醫院自家伺服器跑 AI 病歷判讀：讀完克里夫蘭診所 7,800 多位心臟瓣膜病人 16 年紀錄",
 url="https://thenextweb.com/news/dyania-health-synapsis-ai-cleveland-clinic-nvidia-hospital",
 intro="NVIDIA 11/13 介紹，新創 Dyania Health 的 Synapsis AI 完全在克里夫蘭診所內部的 NVIDIA 伺服器上運作，病歷不出院區。它讀了 7,800 多位 2005～2021 年做過主動脈瓣置換的病人、最長 16 年的醫師筆記與檢查報告，每人回答 88 個臨床問題，每個答案都連回原始病歷出處；整理出的資料被用來建立預測人工瓣膜何時失效的模型，所有醫療決定仍由醫師做。",
 kw="NVIDIA 輝達 Dyania Synapsis 醫療 病歷 克里夫蘭診所 Cleveland Clinic 地端 隱私 心臟 瓣膜 AI 判讀"),
]
ids={x['id'] for x in d}; urls={x['url'] for x in d}
for n in new:
    assert n['id'] not in ids and n['url'] not in urls, (n['id'], n['url'])
    assert n['date']>='2026-09-01'
d=sorted(new+d,key=lambda x:x['date'],reverse=True)
json.dump(d,open('data.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(d), 'added', len(new))
