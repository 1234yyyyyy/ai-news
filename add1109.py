# -*- coding: utf-8 -*-
import json
d=json.load(open('data.json',encoding='utf-8'))
new=[
dict(id="nvidia-board-foreign-intelligence-probe",date="2026-11-08",co="NVIDIA",cos=["NVIDIA"],types=["政策"],
 title="NVIDIA 董事會啟動獨立調查：近期報導指黃仁勳成為外國情報行動對象",
 url="https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors",
 intro="NVIDIA 董事會 11/8 發表聲明，因近期報導指創辦人暨執行長黃仁勳成為外國情報行動對象，啟動由獨立董事組成、並由外部獨立律師協助的調查。董事會表示目前沒有理由認為國家安全或 NVIDIA 機密已遭洩漏，會檢視所有可取得的資訊；黃仁勳支持並承諾配合調查。董事會對他與領導團隊保持信心，並將適時提供後續說明。",
 kw="NVIDIA 董事會 黃仁勳 Jensen Huang 獨立調查 外國情報 國家安全"),
dict(id="anthropic-onepwr-generator-3-4-billion",date="2026-11-08",co="Anthropic",cos=["Anthropic"],types=["投資合作"],
 title="FT：Anthropic 斥約 34 億美元向 OnePWR 預訂 1.7 GW 燃氣發電機，供資料中心用電",
 url="https://www.cnbc.com/2026/11/08/anthropic-generator-deal-ai-data-centers.html",
 intro="《金融時報》11/8 報導，Anthropic 在 9 月底向德州聖安東尼奧設備供應商 OnePWR Solutions 買下約 1.7 GW 重型燃氣發電機承諾，交易約 34 億美元，是目前已知 AI 實驗室最大規模此類採購。CNBC 轉述，Anthropic 並未收購 OnePWR，也沒有員工轉過來，但交易包含安裝所需的工程與施工能力；路透無法立即查證，Anthropic 與 OnePWR 皆未回應置評。路透 9 月曾報導 Anthropic 預期未來 10 年在 AI 基礎建設上投入超過 5,000 億美元。",
 kw="Anthropic OnePWR 發電機 34億 1.7GW 資料中心 電力 FT CNBC"),
dict(id="apple-siri-more-agentic-gurman",date="2026-11-08",co="Apple",cos=["Apple"],types=["產品"],
 title="Bloomberg：執行長 Ternus 要求加快 Siri，目標明年讓它更像能持續執行任務的代理",
 url="https://www.theverge.com/ai-artificial-intelligence/1029552/apple-siri-ai-agentic",
 intro="The Verge 11/8 引述 Bloomberg Mark Gurman 報導，新任執行長 John Ternus 正敦促軟體主管 Craig Federighi 加快 Siri 路線圖，做出能與 OpenAI Dots、Meta Muse 競爭的 AI 代理。未來數月預期兩項改進：iOS 27.3 讓 Siri 更細緻控制蘋果自家 App（例如裁切照片、整理 Safari 分頁）；第三方 App 整合（如透過 Grubhub 下單、OpenTable 訂位）則可能要等到春季。Gurman 表示蘋果希望 Siri 能追蹤目標、判斷下一步並持續推進，而不必使用者逐步下指令，且認為最早明年就可能讓 Siri 更像代理。",
 kw="Apple Siri AI 代理 Ternus Federighi Gurman Bloomberg Dots Muse iOS 27.3"),
dict(id="nvidia-h200-new-matrix-empty-office",date="2026-11-07",co="NVIDIA",cos=["NVIDIA"],types=["晶片"],
 title="紐時：美國核准中國公司處理 NVIDIA H200，其中 New Matrix 辦公室空無一人",
 url="https://www.theverge.com/ai-artificial-intelligence/1029483/nvidia-ai-chips-china-blacklist-government",
 intro="The Verge 11/7 引述《紐約時報》報導，美國商務部核准的 NVIDIA H200 處理商之一 New Matrix，其登記辦公室空無一人，報導形容是「空洞的灰色空殼，天花板垂著本該接燈的電線」。該公司約 17 個月前成立，網上資料極少，所在大樓名錄沒有它，園區物業人員也說沒紀錄；其所有者與一家 2024 年起被美國列入實體清單的中國私募股權公司有關聯。紐時認為這不是個案，而是與受國安貿易限制實體有關的公司獲准購買 NVIDIA 晶片的模式。拜登時期限制對中出售晶片，川普政府在 NVIDIA 同意把銷售抽成 15% 給美國政府後放寬限制。",
 kw="NVIDIA H200 New Matrix 中國 商務部 空殼 實體清單 晶片出口 The Verge 紐時"),
dict(id="microsoft-ai-frontiers-langford-leaves",date="2026-11-06",co="Microsoft",cos=["Microsoft"],types=["政策"],
 title="AI Frontiers 共同組織者 Langford：研究室已被併入 Microsoft AI，他選擇離開",
 url="https://hunch.net/?p=13764006",
 intro="Microsoft Research AI Frontiers 共同組織者 John Langford 11/6（11/7 更新）在個人部落格寫下〈The End of AI Frontiers〉，表示這個約 50 人的小組 9 月初被改組進 Microsoft AI 後，他已安置成員並離開。他寫道，該組多數工作是讓代理能運作，例如 AutoGen 編排框架與 Fara 電腦操作代理；新東家前 Inflection 領導層的核心哲學是「擴大規模，並且積極地不做研究」，把力氣放在資料而非新方法。他說其他創始領導成員似乎也得出類似結論，並宣布來年不會再有該組實習名額。",
 kw="Microsoft AI Frontiers John Langford AutoGen Fara MSR Microsoft AI 擴大規模 研究"),
dict(id="anthropic-claude-max-lawsuit-usage-claims",date="2026-11-06",co="Anthropic",cos=["Anthropic"],types=["價格方案"],
 title="加州聯邦法官：Anthropic Claude Max「5 倍／20 倍用量」宣傳可能誤導，部分訴訟續行",
 url="https://www.courthousenews.com/anthropic-must-face-claims-its-claude-max-pitch-misled-users/",
 intro="Courthouse News 11/6 報導，加州聯邦治安法官 Alex Tse 認為 Anthropic 廣告「可比 Pro 多用 5 倍或 20 倍」可能誤導消費者，允許 Claude 使用者提出的集體訴訟部分主張續行。Anthropic 的 Max 5x 約 100 美元、Max 20x 約 200 美元，對照 Pro 約 17 至 20 美元。原告指出 Max 在每段 5 小時工作階段內確實有 5 倍或 20 倍用量，但週用量上限並非 Pro 的 5 倍或 20 倍；以某一模型估算，Max 20x 週用量約為 Pro 的 6 倍、Max 5x 約 3.5 倍。Tse 寫道相關廣告「表面上可能誤導」，且每次用量說明距離主要銷售頁有兩個超連結之遠。疏忽不實陳述與違反訂閱合約主張續行；部分不公平競爭與禁制令請求被駁回，法官並說 Anthropic 並非用收緊上限當誘餌詐騙。",
 kw="Anthropic Claude Max 5x 20x 用量 訴訟 誤導廣告 Alex Tse Courthouse News Pro"),
dict(id="aws-bedrock-web-answer-agentcore",date="2026-11-05",co="Amazon",cos=["Amazon"],types=["產品"],
 title="AWS Bedrock AgentCore 推出 Web Answer：一次呼叫就回附出處的網路答案，每千次 10 美元",
 url="https://aws.amazon.com/about-aws/whats-new/2026/11/web-answer-amazon-bedrock/",
 intro="AWS 11/5 宣布 Amazon Bedrock AgentCore 的 Web Answer 正式推出：代理送出自然語言問題，即可在單次工具呼叫中取得綜合、有出處的答案，不必自建搜尋、擷取、撰寫與引用流程。它會自行規劃並平行搜尋、判斷證據是否足夠，支援網域允許／拒絕清單與發布日期篩選，掛在 AgentCore Gateway 上透過 MCP 呼叫，以 IAM 驗證，並宣稱查詢不外洩。服務先在美國東部（維吉尼亞北部）提供；AWS 官方部落格寫明定價為每 1,000 次工具呼叫 10 美元。",
 kw="AWS Amazon Bedrock AgentCore Web Answer MCP 引用 搜尋 代理 定價"),
dict(id="google-xla-serving-engine-opensource",date="2026-11-05",co="Google",cos=["Google"],types=["產品"],
 title="Google 開源 XLA Serving Engine：用 C++ 上線推論，短請求吞吐量稱可達 Python 伺服器 2 至 5 倍",
 url="https://opensource.googleblog.com/2026/11/supercharging-xla-inference-xla-serving-engine.html",
 intro="Google 11/5 在開源部落格宣布推出 XLA Serving Engine（XSE），採 Apache 2.0 授權，讓工程師用 Python（JAX、PyTorch）訓練後匯出為含 StableHLO 的 XLA SavedModel，再由 C++ 執行期載入，避開正式環境的 Python 負擔。Google 內部研究稱，短請求吞吐量可達其所能打造的最佳 Python 伺服器 2 至 5 倍（相較簡易實作則為 8 至 36 倍），每次預測 CPU 時間少 30% 至 70%、記憶體約四分之一。XSE 已是 Google 內部正式基礎建設，宣稱每秒處理超過 600 萬次查詢，用於 YouTube Shorts、Google Ads、Search 與部分 Gemini Omni。公司建議大型長上下文自回歸語言模型仍用 vLLM 或 SGLang。",
 kw="Google XLA Serving Engine XSE OpenXLA Apache C++ 推論 TPU JAX Gemini Omni"),
]
ids={x['id'] for x in d}; urls={x['url'] for x in d}
for n in new:
    assert n['id'] not in ids and n['url'] not in urls, (n['id'], n['url'])
    assert n['date']>='2026-09-01'
d=new+d
json.dump(d,open('data.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(d), 'added', len(new))
