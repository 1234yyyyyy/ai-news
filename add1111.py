# -*- coding: utf-8 -*-
import json
d=json.load(open('data.json',encoding='utf-8'))
new=[
dict(id="xai-grok-build-share-links-leak",date="2026-11-11",co="xAI",cos=["xAI"],types=["政策"],
 title="Ars Technica：Grok Build 分享連結可被列舉，約 3.5 萬個 App 資料外露，連 SpaceXSI 自家機密也在內",
 url="https://arstechnica.com/security/2026/11/grok-build-coding-agent-leaks-oodles-of-confidential-info-some-belonging-to-spacexsi/",
 intro="Ars Technica 11/11 報導，資安公司 Claroc 研究發現，SpaceXSI（SpaceX 與 xAI 合併後的公司）的 vibe coding 代理 Grok Build 雖把分享網址隨機化，但設計上的缺陷讓任何人都能列舉出數千個上線中的專案，約 3.5 萬個 App 門戶大開，點開就看得到裡面的資料，包括內部商業計畫、廣告提案、體檢結果、員工姓名與編號。其中 24 個是 SpaceXSI 自己做的 App，含標示機密的企業業務新人到職計畫與 594 個客戶的業務版圖。Claroc 週日通報未獲回應，Ars 去信詢問後數小時內，SpaceXSI 的 24 個 App 連結已失效，其他用戶資料當時多半仍可存取。",
 kw="xAI SpaceXSI Grok Build vibe coding 資料外洩 分享連結 Claroc Ars Technica 資安"),
dict(id="anthropic-ipo-roadshow-70-78",date="2026-11-10",co="Anthropic",cos=["Anthropic"],types=["投資合作"],
 title="Anthropic 啟動 IPO 路演：發行 8.25 億股、每股 70 至 78 美元，申請以「ANT」在 Nasdaq 掛牌",
 url="https://www.anthropic.com/news/roadshow-launch",
 intro="Anthropic 11/10 宣布啟動 A 類普通股首次公開發行的路演：擬發行 8.25 億股，其中約 8.01 億股由公司發行、約 2,365 萬股由部分現有股東出售（公司不取得這部分收益），另給承銷商 30 天內加購最多 1.2375 億股的選擇權。預期發行價每股 70 至 78 美元，已申請在 Nasdaq Global Select Market 以代號「ANT」掛牌，主辦承銷商包括高盛與摩根士丹利。註冊聲明已送交美國 SEC 但尚未生效。",
 kw="Anthropic IPO 路演 上市 Nasdaq ANT 發行價 70 78 美元 8.25億股 高盛 摩根士丹利"),
dict(id="anthropic-claude-meetings-whiteboards-sheets",date="2026-11-10",co="Anthropic",cos=["Anthropic"],types=["產品"],
 title="Anthropic 推 Claude Meetings：Claude 進視訊會議邊聽邊做事，另推 Whiteboards 白板與 Sheets 試算表",
 url="https://techcrunch.com/2026/11/10/anthropic-launches-claude-meetings-to-turn-workplace-discussions-into-plans-and-tasks/",
 intro="TechCrunch 11/10 報導，Anthropic 推出 Claude Meetings：團隊可把 Claude 以可見參與者身分加進視訊會議，它會跟著討論即時起草計畫、在白板上排時間線、回答會議聊天室問題，並從連接的工作 App 調資料；會後筆記與待辦都存在 claude.ai。Claude 會在聊天室表明身分，未經管理員授權不會加入有外部來賓的會議，外部來賓一進來就自動離開。Meetings 先以測試版提供給 Team 與 Enterprise 方案，目前只支援 Google Meet。同時推出的 Claude Whiteboards（付費方案測試版，網頁、桌面、手機皆可）能把白板轉成文件或簡報，Claude Sheets 則能一起建立和編輯試算表。",
 kw="Anthropic Claude Meetings 會議 Whiteboards 白板 Sheets 試算表 Google Meet Team Enterprise 辦公套件"),
dict(id="openai-chatgpt-business-hub-profiles",date="2026-11-10",co="OpenAI",cos=["OpenAI"],types=["產品"],
 title="OpenAI 推 ChatGPT 商家專頁 Business Hub：企業可認證、更新資訊、看曝光數據，還能上架商家代理",
 url="https://techcrunch.com/2026/11/10/openai-rolls-out-new-business-profiles-making-chatgpt-just-a-little-bit-more-like-google/",
 intro="TechCrunch 11/10 報導，OpenAI 推出測試版 Business Hub：企業可建立並認證商家資料、更新產品與服務資訊，類似 Google 商家檔案；符合資格的公司還能上架專屬商家代理，讓 ChatGPT 使用者直接詢問該公司與產品。Business Hub 也提供有限的洞察數據，包括資料頁瀏覽、商家被提及次數與網站點擊。OpenAI 營利化副總裁 Benji Shomair 表示會依不同業種與市場採用多種認證方式。報導指出，OpenAI 先前以抽成方式讓使用者在 ChatGPT 直接購物的嘗試未能起飛，已於 3 月收掉。",
 kw="OpenAI ChatGPT Business Hub 商家專頁 商家代理 認證 洞察 數據 Google 商家 電商 Shomair"),
dict(id="openai-acquires-odessia-travel",date="2026-11-10",co="OpenAI",cos=["OpenAI"],types=["投資合作"],
 title="OpenAI 收購 AI 旅遊代理新創 Odessia：Sonder 創辦人 Davidson 加入，協助打造旅遊體驗",
 url="https://techcrunch.com/2026/11/10/openai-acquires-odessia-travel-startup-created-by-sonder-founder/",
 intro="TechCrunch 11/10 報導，AI 旅遊代理 Odessia 創辦人 Francis Davidson 宣布公司被 OpenAI 收購，他已加入 OpenAI 協助規劃旅遊的未來，OpenAI 發言人也證實此事；交易條件未公開，看來屬於延攬人才型收購。Odessia 成立約一年，曾獲 Sequoia 領投 600 萬美元種子前輪，約五個月前推出，工具已停止服務。OpenAI 尚未宣布旅遊相關新產品，但表示旅遊是使用者常問的領域，並稱每週有 12 億人用 ChatGPT 處理日常事務。Davidson 先前創辦短租公司 Sonder。",
 kw="OpenAI 收購 Odessia 旅遊 AI 代理 Francis Davidson Sonder Sequoia 人才收購 ChatGPT"),
dict(id="google-gemini-robotics-2-5",date="2026-11-10",co="Google",cos=["Google"],types=["模型"],
 title="Google DeepMind 發表 Gemini Robotics 2.5：200 項任務成功率高 30% 至 100%，賓士產線取放零件達 96%",
 url="https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/",
 intro="Google DeepMind 11/10 發表 Gemini Robotics 2.5，是目前最強的視覺語言動作（VLA）模型，擴大機器人能學的技能並加快學習速度。在 200 多項任務（例如用夾子上菜、綁禮盒蝴蝶結、移液）評測中，成功率比先前基準高 30% 至 100%、完成速度快 20% 至 30%。在賓士產線的實地概念驗證中，協助 Apptronik 的 Apollo 2 人形機器人揀選和包裝汽車零件，成功率 96%。DeepMind 也加強實體安全可控性，並推出針對機器人越獄攻擊的新基準；模型正陸續提供給機器人合作夥伴。",
 kw="Google DeepMind Gemini Robotics 2.5 VLA 機器人 人形機器人 Apptronik Apollo 賓士 Mercedes-Benz 靈巧度"),
dict(id="google-cloud-gemini-for-healthcare",date="2026-11-10",co="Google",cos=["Google"],types=["產品"],
 title="Google Cloud 推 Gemini for healthcare：整合病歷、帳務與指引，自動跑病歷彙整與事前授權審查",
 url="https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/gemini-for-healthcare/",
 intro="Google Cloud 11/10 宣布 Gemini for healthcare，用專門技能與資料連接器串起既有第三方系統，把電子病歷、帳務平台、臨床指引與 Medicare 資料集整合在一起，在設定好的防護規則與人員監督下，執行病歷彙整、事前授權審查等多步驟流程。Google 指出臨床人員每週約有 28 小時花在文書與行政工作。目前以預覽版提供，首批合作夥伴包括 HCA Healthcare、Highmark Health 與 Northwell Health。",
 kw="Google Cloud Gemini for healthcare 醫療 病歷 事前授權 EHR Medicare HCA Northwell Highmark 代理"),
dict(id="meta-muse-ember-small-model",date="2026-11-09",co="Meta",cos=["Meta"],types=["模型"],
 title="Meta 推最小最省的 Muse Ember：代理重複任務專用，每百萬 token 輸入 0.10、輸出 0.50 美元",
 url="https://research.meta.ai/blog/muse-ember",
 intro="Meta 11/9 推出 Muse Ember，是旗下最小、最有效率的模型，專做代理整天重複的工作：工具呼叫、程式子任務、路由、資料擷取與長文件解析。Meta 稱它以約三分之一成本達到 Claude Haiku 5.5 的最佳分數，並勝過 GPT-6 Luna 所有推理設定，在 Artificial Analysis 排行榜的成本效率前緣上；例如 AutomationBench-AA 得 37.8（Haiku 5.5 為 13.9）、Terminal-Bench 4.0 得 40.9。已在 Meta Model API 上架，200K token 以內每百萬輸入 0.10 美元、輸出 0.50 美元，更長的提示則為 0.30／1.50 美元。",
 kw="Meta Muse Ember 小模型 代理 低成本 Meta Model API Claude Haiku 5.5 GPT-6 Luna Artificial Analysis 定價"),
dict(id="microsoft-ibm-imagine-enterprise",date="2026-11-10",co="Microsoft",cos=["Microsoft"],types=["投資合作"],
 title="IBM 與微軟推 Imagine Enterprise 代理平台：主打受監管產業，附 6,000 多個現成 AI 代理",
 url="https://news.microsoft.com/source/2026/11/10/ibm-and-microsoft-announce-a-new-ai-agent-platform-designed-for-industry-specific-transformation/",
 intro="IBM 與微軟 11/10 宣布推出 Imagine Enterprise，協助企業（尤其是受監管產業）建立、執行與治理處理產業特定流程的 AI 代理，並為符合資格的案子派駐雙方的前線工程師。IBM Consulting 帶來以 IBM Consulting Advantage 打造的 6,000 多個 AI 代理與資產，微軟則提供 AI、資料、雲端與資安基礎，包括 Microsoft Foundry、GitHub Copilot、Copilot Studio 協調代理，以及 Fabric 與 Microsoft 365 基礎設施；平台內建控管、可觀測性與 AI 合規支援，可接上企業既有的資料與系統。",
 kw="Microsoft IBM Imagine Enterprise AI 代理 平台 受監管產業 IBM Consulting Foundry Copilot Studio 治理"),
dict(id="apple-harbor-local-ai-mac-cluster",date="2026-11-10",co="Apple",cos=["Apple"],types=["產品"],
 title="9to5Mac：蘋果開發 Harbor App，讓 Mac 變私人 AI 推論伺服器，可用 Thunderbolt 5 串多台合併記憶體",
 url="https://9to5mac.com/2026/11/10/apple-has-new-mac-app-coming-to-make-running-local-ai-models-easy/",
 intro="9to5Mac 11/10 報導，爆料者 Aaron Perris 發現蘋果正在開發名為 Harbor 的 Mac App，標榜「把你的 Mac 變成私人 AI 推論伺服器」：在 Apple Silicon 上本機執行開放權重模型，資料不上雲。它能自動偵測透過 Thunderbolt 5 連接的多台 Mac 組成叢集，合併統一記憶體來跑單台裝不下的大模型或服務更多並行請求，免指令列設定，也能在 App 內瀏覽、下載和載入模型。Harbor 目前以蘋果旗下 Claris 品牌進行私人預覽，報導認為可能在未來數週到數月內公開。",
 kw="Apple 蘋果 Harbor Mac 本機 AI 推論 開放權重 Thunderbolt 5 叢集 統一記憶體 Claris 9to5Mac"),
]
ids={x['id'] for x in d}; urls={x['url'] for x in d}
for n in new:
    assert n['id'] not in ids and n['url'] not in urls, (n['id'], n['url'])
    assert n['date']>='2026-09-01'
d=new+d
json.dump(d,open('data.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(d), 'added', len(new))
