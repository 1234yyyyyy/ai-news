# -*- coding: utf-8 -*-
import json
d=json.load(open('data.json',encoding='utf-8'))
new=[
dict(id="openai-hacktron-partnership",date="2026-11-06",co="OpenAI",cos=["OpenAI"],types=["政策"],
 title="OpenAI 與 Hacktron 合作找自家系統漏洞，並擴大 Daybreak Red 存取",
 url="https://openai.com/index/partnering-with-hacktron/",
 intro="OpenAI 11/6 宣布與資安新創 Hacktron 合作，雙方工程師與安全研究員共同鎖定高優先測試範圍，重點放在 OpenAI 系統與第三方服務的交界。Hacktron 擅長以 AI 代理做程式碼審查、滲透測試與紅隊演練，雙方因 Bug Bounty 結識；合作並擴大 Hacktron 透過 Daybreak Red 使用前沿模型。OpenAI 同週也讓 Cathedral 研究員加入下一輪安全衝刺，並提高漏洞賞金。",
 kw="OpenAI Hacktron Daybreak Red 漏洞 Bug Bounty 紅隊 第三方整合 資安 Cathedral"),
dict(id="openai-biobasicsbench",date="2026-11-06",co="OpenAI",cos=["OpenAI"],types=["模型"],
 title="OpenAI 推 BioBasicsBench：100 項濕實驗日常任務，GPT-6 Astra 拿 66.7%",
 url="https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science",
 intro="OpenAI 11/6 與生技公司 Ligo 發表 BioBasicsBench，用 100 項真實濕實驗任務評測 AI 代理解讀凝膠、顯微鏡、儀器匯出與定序等原始資料的能力。xhigh 推理設定下 GPT‑6 Astra 平均拿到 66.7% 可用分數，優於 GPT‑5.6 Sol 的 43.8%；評測涵蓋七款模型、37 種設定共 18,500 次結果。基準強調錯誤偵測、對照組檢查，以及承認證據不足，目標協助生物研究日常分析並評估生物安全意涵。",
 kw="OpenAI BioBasicsBench 濕實驗 Ligo GPT-6 Astra 基準 生物學 多模態 生物安全"),
dict(id="openai-friar-datacenter-funding",date="2026-11-06",co="OpenAI",cos=["OpenAI"],types=["投資合作","政策"],
 title="OpenAI CFO Friar：中期選舉後仍續砸資料中心，已關 110 億美元融資首批",
 url="https://www.cnbc.com/2026/11/06/open-ai-data-centers-election.html",
 intro="CNBC 報導，OpenAI 財務長 Sarah Friar 11/6 在 Citi TMT 高峰會表示，儘管美國中期選舉多地通過限制資料中心發展的公投，公司仍會持續投資基礎設施並募資以滿足客戶需求。她說公司持續評估 2027 年上市；CNBC 證實本輪融資已關 110 億美元首批，未來數週還可再募最多約 90 億。Friar 並稱 OpenAI 正以約 1.25 兆美元估值洽談募資，且前一日已公布面向社區的算力園區承諾。",
 kw="OpenAI Sarah Friar 資料中心 中期選舉 融資 110億 IPO 2027 CNBC Citi TMT"),
dict(id="meta-muse-spaces",date="2026-11-06",co="Meta",cos=["Meta"],types=["產品"],
 title="Meta Muse 推 Spaces：用一句話建專屬空間，可排進側欄與主分頁",
 url="https://about.fb.com/news/2026/11/introducing-spaces-customize-muse-app/",
 intro="Meta 11/6 在 Muse App 推出 Spaces：用自然語言描述想法（禮物追蹤、行程板、婚禮規劃等），Muse 會建成可互動的專屬體驗，並可放到側欄或主分頁、排程何時顯示。Spaces 可串接常用 App，在背景自動更新演唱會檔期、價格或儲蓄進度；目前 Muse 上線地區皆可用，之後還會探索分享與協作。同日也強調會把從 Muse Wonder 學到的特化模型能力滾進 Muse。",
 kw="Meta Muse Spaces 客製空間 側欄 分頁 App串接 Wonder Zuckerberg 產品"),
dict(id="meta-specialized-models-muse",date="2026-11-06",co="Meta",cos=["Meta"],types=["模型","產品"],
 title="Meta 把 Muse Wonder 特化模型導入 Muse／Meta AI：記憶力與任務完成大升",
 url="https://research.meta.ai/blog/specialized-models-for-muse-and-metaai",
 intro="Meta AI Research 11/6 宣布，以 Muse Wonder 訓練的特化模型開始導入 Muse 與 Meta AI。Personal Superintelligence Index 從 38% 升到 47%；Active Memory 讓關鍵資訊遺忘降約 2.4 倍、評測正確使用關鍵脈絡從 76% 到 90%；Active Focus 在突發阻礙下完成日常任務改善 67%。目標讓更多用戶用到更強的記憶、多工與目標追蹤能力。",
 kw="Meta Muse Wonder 特化模型 Active Memory Active Focus Personal Superintelligence Index Meta AI"),
dict(id="anthropic-project-eve",date="2026-11-06",co="Anthropic",cos=["Anthropic"],types=["模型"],
 title="Anthropic Project EVE：Claude 玩 EVE 線上遊戲，測交易獲利與隊友破壞偵測",
 url="https://www.anthropic.com/research/project-eve-claude-plays-mmorpgs",
 intro="Anthropic 11/6 公開 Fellows 計畫研究成果 Project EVE：與 Fenris Creations 合作，讓 Claude 在 EVE Online 市場模擬與 EVE Frontier 實況中長期行動。EVE Online 上較新模型 Fable 5 六個月平均把本金做到約六倍，多採低風險價差套利；方向性押注則約半數獲利。EVE Frontier 四機團隊能協調，但被指示暗中破壞的隊友幾乎抓不到，凸顯多智能體信任與稽核需求。",
 kw="Anthropic Project EVE Claude Fable 5 EVE Online Frontier 多智能體 紅隊 交易 Fenris"),
dict(id="amazon-alexa-shopping-text",date="2026-11-06",co="Amazon",cos=["Amazon"],types=["產品"],
 title="Amazon Alexa for Shopping 開放簡訊購物：美區邀請制，數週內擴大",
 url="https://www.aboutamazon.com/news/retail/alexa-for-shopping-text-to-shop",
 intro="Amazon 11/6 宣布 Alexa for Shopping 支援簡訊：受邀美區用戶可傳訊「Alexa Shopping」搜商品、組購物車、下單、追價與傳照片找相似款，也可串 Shop Direct 找站外商品。過去 12 個月逾 4 億人用過 Alexa for Shopping，代理式功能用戶自年初成長逾 8 倍；今日起小範圍邀請，數週內擴至更多用戶，對話還可在 App、網站與裝置間延續。",
 kw="Amazon Alexa for Shopping 簡訊 文字購物 美區 邀請制 Shop Direct 代理 購物車"),
dict(id="microsoft-neocloud-consolidation",date="2026-11-06",co="Microsoft",cos=["Microsoft"],types=["投資合作"],
 title="微軟擬縮減 neocloud 夥伴、不續約 Oracle：轉向自建資料中心",
 url="https://www.cnbc.com/2026/11/06/microsoft-moves-to-consolidate-its-relationships-with-neoclouds-in-ai.html",
 intro="CNBC 11/6 引述知情人士報導，微軟正評估縮減 neocloud（如 CoreWeave、Nebius、Chronoscale、IREN、Lambda、Nscale 等）合作名單，優先自建資料中心並保留少數關鍵供應商；兩名消息人士稱已決定不續約 Oracle 的容量協議。發言人強調策略是自有、租賃與第三方並用並依需求調整。同日 IREN 交出容量後因網通升級延至明年初上線，顯示 AI 基建交付壓力升高。",
 kw="Microsoft neocloud CoreWeave Nebius Oracle IREN 資料中心 Azure GPU CNBC"),
dict(id="google-wyoming-17b-data-center",date="2026-11-05",co="Google",cos=["Google"],types=["投資合作","政策"],
 title="Google 宣布懷俄明州首座資料中心：砸 170 億美元、702 MW 燃料電池加碳捕捉",
 url="https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/wyoming-data-center/",
 intro="Google 11/5 宣布在懷俄明州 Laramie County 蓋首座資料中心，長期投資 170 億美元，並與 Tallgrass、Black Hills Energy、AEP、Related Digital 合作。計畫採美國製 Bloom Energy 燃料電池，簽約 702 MW 商用規模燃料電池加碳捕捉與地質封存（CCS），並採氣冷以降低用水；Google 承諾自付所用电費與相關基礎設施成本，並成立社區委員會回應地方意見。",
 kw="Google Wyoming 資料中心 170億 燃料電池 702MW CCS Bloom Energy Cheyenne 社區"),
dict(id="metr-anthropic-ai-rd-acceleration",date="2026-11-05",co="Anthropic",cos=["Anthropic"],types=["政策"],
 title="METR：Anthropic 能力進度約加速至以往兩倍，多數證據遭遮罩",
 url="https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/",
 intro="獨立評測組織 METR 11/5 公布對 Anthropic 的高存取評估：自 2025 年 10 月起，內部 AECI 基準分數成長約為歷史速度的 1.9 倍（95% CI 1.5–2.8），亦即過去一年約等同先前兩年進度；加速並非來自訓練算力擴張加速，METR 估計目前多數（約八成）可歸因於 AI 輔助研發。報告約百頁，Anthropic 遮罩多數關鍵證據，公眾難自行核對細節。",
 kw="METR Anthropic AI R&D 加速 AECI 1.9倍 紅隊 風險 RSP 遮罩"),
]
ids={x['id'] for x in d}; urls={x['url'] for x in d}
for n in new:
    assert n['id'] not in ids and n['url'] not in urls, (n['id'], n['url'])
    assert n['date']>='2026-09-01'
d=new+d
json.dump(d,open('data.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(d))
for n in new:
    print(n['date'], n['id'], n['co'])
