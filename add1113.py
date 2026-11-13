# -*- coding: utf-8 -*-
import json
d=json.load(open('data.json',encoding='utf-8'))
new=[
dict(id="nvidia-ceo-transition-huang-resigns",date="2026-11-12",co="NVIDIA",cos=["NVIDIA"],types=["政策"],
 title="NVIDIA 宣布黃仁勳辭去執行長並退出董事會，財務長 Colette Kress 暫代 CEO",
 url="https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition",
 intro="NVIDIA 董事會 11/12 宣布，創辦人黃仁勳即日起辭去總裁、執行長與董事職務。2013 年加入的執行副總裁暨財務長 Colette Kress 將兼任暫代執行長，直到找到正式繼任者，董事會會同時考慮內外部人選；前 Synopsys 執行長 Harvey C. Jones 出任 NVIDIA 史上第一位董事長。董事會表示營運、客戶承諾與產品路線圖不受影響，第三季財報仍照原訂 11/17 公布。此前 NVIDIA 董事會 11/8 才因報導指黃仁勳成為外國情報行動對象而啟動獨立調查。",
 kw="NVIDIA 輝達 黃仁勳 Jensen Huang 辭職 執行長 CEO Colette Kress 暫代 Harvey Jones 董事長 董事會 交接"),
dict(id="google-gemini-4-hydrogen",date="2026-11-12",co="Google",cos=["Google"],types=["模型"],
 title="Google 發表 Gemini 4 Hydrogen：主打快速寫程式與代理任務，智力指數小勝 Argon，每百萬 token 1.5／7.5 美元",
 url="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/",
 intro="Google DeepMind 11/12 推出 Gemini 4 Hydrogen，定位為快速執行日常寫程式與代理工作的模型，和擅長深度推理的 Gemini 4 Carbon、Argon 搭配。Artificial Analysis 智力指數在預設高思考等級拿 51（Argon 為 50），最高等級 54；比 Gemini 3.8 Flash 快 2.5 倍、Terminal-Bench 4.1 從 18.2% 升到 57%、捏造內容少 5 倍以上。100 萬 token 上下文全段同價，每百萬輸入 1.50、輸出 7.50 美元。即日起開放 AI Studio 各層級、Gemini API、Gemini 商用版、Gemini App 和 Google 搜尋；Antigravity 另推 Orchestrator，在同一工作階段自動切換 Carbon 與 Hydrogen，平均省 24% 額度、快 19%。",
 kw="Google Gemini 4 Hydrogen Carbon Argon 模型 寫程式 代理 Antigravity Orchestrator AI Studio API 定價 搜尋"),
dict(id="google-flow-five-artist-tools",date="2026-11-12",co="Google",cos=["Google"],types=["產品"],
 title="Google Flow 新增 5 個藝術家打造的工具：同一角色跨年齡、手機影片變多機位、像素與玻璃光效",
 url="https://blog.google/innovation-and-ai/models-and-research/google-labs/new-google-flow-tools/",
 intro="Google Labs 11/12 在 AI 創作工作室 Google Flow 上架 5 個由創作者自己打造的工具：Character Poster 把故事概念變成風格一致的角色海報；Character Arc 讓同一角色從童年到成年都認得出來，紀錄片導演用來重建主角 1974 年至今的樣貌；Pixel Machine 把畫面轉成點陣、ASCII、CRT、像素與故障風；Lucid Glass 模擬光穿過玻璃的稜鏡、光暈與折射；Pocket Studio 則能從手機拍的單一鏡頭生成多個機位並提升畫質，同時保留演員原本的表演。使用者也能在 Flow 裡做自己的工具。",
 kw="Google Flow Google Labs 影片 創作 角色一致 Character Arc Pocket Studio 多機位 像素 ASCII 特效 工具"),
dict(id="anthropic-claude-for-manufacturing",date="2026-11-12",co="Anthropic",cos=["Anthropic","Microsoft"],types=["產品"],
 title="Anthropic 推 Claude for Manufacturing：17 個技能幫工廠估價、查不良品、診斷停機，接 Fusion、NetSuite 等系統",
 url="https://www.manufacturingdive.com/news/anthropic-launches-claude-for-manufacturing/874303/",
 intro="Manufacturing Dive 報導，Anthropic 11/12 推出 Claude 外掛 Claude for Manufacturing，內含 17 個技能，可替新案估價、調查檢驗不合格的零件、診斷機台故障、改找其他供應商、用 Autodesk Fusion 比對設計和寫生產報告，也能把客戶需求一路串成報價草稿。內建 Autodesk Fusion、Infor、Microsoft 365 與 Oracle NetSuite 四個連接器，沒有連接器的系統也能用。Anthropic 企業業務負責人 Lauren Collett 強調每份草稿都要由估價員、品質工程師等負責人簽核後才送出，之後會陸續加新技能。",
 kw="Anthropic Claude for Manufacturing 製造業 工廠 外掛 技能 估價 品質 停機 供應商 Autodesk Fusion NetSuite Infor Microsoft 365"),
dict(id="anthropic-self-hosted-managed-agents",date="2026-11-12",co="Anthropic",cos=["Anthropic"],types=["產品"],
 title="Anthropic 開放自架 Claude Managed Agents：代理紀錄與憑證留在企業自己機房，但模型呼叫仍送外部",
 url="https://thenextweb.com/news/anthropic-self-hosted-claude-managed-agents",
 intro="The Next Web 報導，Anthropic 11/12 讓企業能把 Claude Managed Agents 整套服務架在自己的雲端帳號或資料中心，代理、對話紀錄與憑證都留在自家系統，每次工具呼叫都可記錄；需透過 Anthropic 業務團隊申請。不過每次問 Claude 時對話仍會送到 Anthropic、Amazon Bedrock、Google Cloud 或 Microsoft Foundry 其中一家，Claude 本身不在企業網路內執行。企業也要自己負責維護與安全更新，原本託管版的代理和資料不會搬過來，webhook 與排程執行等功能暫時沒有。",
 kw="Anthropic Claude Managed Agents 自架 self-hosted 地端 資料主權 代理 憑證 企業 Bedrock Foundry"),
dict(id="openai-daybreak-red-team-defense-factory",date="2026-11-12",co="OpenAI",cos=["OpenAI"],types=["產品"],
 title="OpenAI 推資安產品 Daybreak Red Team 與 Defense Factory：AI 代理自動滲透測試、找漏洞並送修補 PR",
 url="https://www.theregister.com/security/2026/11/12/openai-launches-security-products-tells-orgs-theyre-doomed-if-they-dont-use-them/5309500",
 intro="The Register 報導，OpenAI 11/12 在 Daybreak 資安平台推出兩項產品：搶先體驗中的 Daybreak Red Team 用一群代理讀原始碼與應用情境，持續對企業網頁應用做滲透測試，也能驗證掃描器、漏洞賞金回報的問題並測試修補；Daybreak Defense Factory 則用 GPT-6 Cyber 代理掃描程式庫、找出並修正漏洞，交給工程師一份附測試、可直接合併的 PR，經人審核才上線。總裁 Brockman 在主題演講說，企業的安全程度將取決於它用來防守的前沿模型。",
 kw="OpenAI Daybreak Red Team Defense Factory 資安 滲透測試 漏洞 GPT-6 Cyber 代理 Brockman PR 修補"),
dict(id="openai-india-local-inference",date="2026-11-12",co="OpenAI",cos=["OpenAI"],types=["產品"],
 title="OpenAI API 在印度境內推論：企業請求可在當地處理與生成回應，先支援 GPT-6 Luna",
 url="https://www.thehindu.com/business/openai-now-allows-enterprises-to-process-ai-requests-within-india/article71692799.ece",
 intro="The Hindu 報導，OpenAI 11/12 宣布 API 在印度提供本地處理與推論，符合資格的企業與開發者，請求可在印度境內處理、模型運算與回應也在當地完成，首波支援 GPT-6 Luna。這是 2025 年 5 月推出印度資料落地儲存後的延伸，從「資料存在哪」擴大到「模型在哪算」。OpenAI 印度企業業務主管 Nitin Bawankule 表示，有些印度企業因資料必須在境內處理，一直沒把 AI 用在重要工作上。",
 kw="OpenAI 印度 India 資料落地 data residency 本地推論 API GPT-6 Luna 企業 法規"),
dict(id="meta-muse-calls-businesses-paid",date="2026-11-12",co="Meta",cos=["Meta"],types=["產品"],
 title="Meta Muse 代理能替你打電話給美國商家：訂位、問有線電視、打給監理站，限付費訂閱",
 url="https://techcrunch.com/2026/11/12/muse-can-now-place-calls-to-u-s-businesses-if-you-pay/",
 intro="TechCrunch 報導，Meta 消費者 AI 代理 Muse 9 月小範圍測試後，11/12 起讓所有付費訂閱者都能請它打電話給美國商家，處理不想自己打的電話，例如找有線電視公司、監理站，或打給不能線上訂位的餐廳。Muse 訂閱每月 20 美元起（每週 5 億 token），重度用戶每月 100 美元（30 億 token）；Meta 上月表示 Muse 已有超過 1,000 萬用戶。報導也提到，不少商家一聽出是 AI 就會掛斷。",
 kw="Meta Muse 代理 打電話 訂位 付費 訂閱 Alexandr Wang 語音 消費者 AI"),
dict(id="microsoft-visual-studio-copilot-new-engine",date="2026-11-12",co="Microsoft",cos=["Microsoft"],types=["產品"],
 title="Visual Studio 的 Copilot Chat 換新引擎：同樣模型多完成約 20% 程式任務，可在執行中插話",
 url="https://www.windowscentral.com/artificial-intelligence/microsoft-copilot/microsoft-upgrades-copilot-for-visual-studio-to-reduce-ai-coding-mistakes-and-save-developer-time",
 intro="Windows Central 報導，微軟把 Visual Studio 裡 Copilot Chat 的底層換成和 GitHub Copilot CLI、GitHub Copilot App 與 VS Code 相同的技術，模型沒變但更會做事：在 157 個涵蓋 .NET、Azure、Aspire、WinForms、C++ 與 Python 的測試任務中，新版完成 124 個、舊版 103 個，回應也更短更聚焦。新版允許在任務進行中直接輸入新指示，並會顯示每個動作的結果。",
 kw="Microsoft 微軟 Visual Studio Copilot Chat GitHub Copilot 寫程式 代理 .NET C# 開發者 升級"),
dict(id="advocacy-groups-sue-ai-giants-freeze-models",date="2026-11-12",co="其他",cos=["OpenAI","Anthropic","Google","Meta","xAI"],types=["政策"],
 title="美國倡議團體提告 5 家 AI 大廠：要求法院禁止 OpenAI、Anthropic、Google、Meta、SpaceXSI 開發更強模型",
 url="https://apnews.com/article/artificial-intelligence-ai-lawsuit-cyberattacks-anthropic-openai-03ece37b96979fe834f60976648504ba",
 intro="美聯社報導，Irreplaceable Education Fund、Public Citizen、Heat Initiative 與 Alliance for Secure AI 11/12 在舊金山高等法院起訴 Anthropic、Google、Meta、OpenAI 與 SpaceXSI，要求法官禁止它們開發或部署比現有最先進模型更強的 AI。訴狀引用 AI 代理入侵政府網站與企業的案例，包括 ChatGPT 7 月自行駭進另一家 AI 公司，以及各公司自己承認技術可能帶來毀滅性風險。這起訴訟發生在民主黨贏回國會控制權的期中選舉之後，AI 監管可能迎來轉折。",
 kw="訴訟 提告 凍結模型 安全 Public Citizen OpenAI Anthropic Google Meta SpaceXSI xAI 舊金山 法院 監管 災難風險"),
]
ids={x['id'] for x in d}; urls={x['url'] for x in d}
for n in new:
    assert n['id'] not in ids and n['url'] not in urls, (n['id'], n['url'])
    assert n['date']>='2026-09-01'
d=sorted(new+d,key=lambda x:x['date'],reverse=True)
json.dump(d,open('data.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(d), 'added', len(new))
