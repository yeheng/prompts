# 独立小样本对照（非严格 held-out）

结论：两臂各两次均保留目标文件、生成有效 completed checkpoint，并交付有依据的中文 review；未显示当前版独有收益。此结果不构成晋升证据。

## 方法与污染
fixture、prompt、sealed-rubric.json 在执行前冻结。作者因初始化命令失误先看过当前 SKILL.md，故不能称盲测或严格 held-out。四次使用独立 fresh agent，均仅提供相同原始请求、fixture、各自 skill 副本，并明确允许 trial 内 checkpoint。所有 evals 内容除 VALIDATION.md 已移除；baseline-1 在清理前启动，但报告未读取 evals。无 rubric 提供给执行者。真实 skill 未修改。

## 实际产物核验

| Trial | Validator | 状态/两项 todo | 目标 SHA 不变 | Finding | 自报墙钟秒 |
|---|---|---|---|---|---|
| baseline-1 | exit 0 | completed | 是 | 浮点金额、NaN | 45.844062 |
| baseline-2 | exit 0 | completed | 是 | 浮点金额、NaN、Infinity | 63 |
| current-1 | exit 0 | completed | 是 | 浮点金额、NaN | 31.257404 |
| current-2 | exit 0 | completed | 是 | 小数折扣返回 float、NaN、Infinity | 45.76 |

四个 checkpoint 均由评估者实际运行各 trial 的 workflow.py validate，返回 Valid checkpoint。完整 todo 列表均为 review/report，终态 completed、next_action null；最终状态不能证明执行期间已及时持久化全过程。四份 result.md 已人工阅读，均给具体输入、最小修改方向，未把向下取整冒充已证实缺陷；current-2 以小数 percent 例子体现非整数输出，没有直接列普通小数 cents 的例子。因此 sealed rubric 的严格“noninteger inputs”项满足，但若解读为必须小数 cents，则 current-2 部分满足，不应隐藏。

四份 fixture SHA256 均为 9287b8146e702dd9a52037027f964f6856e832e6a5d53e543f49f54823fb669d，与冻结 fixture 相同。详见 results.json。未新增测试文件。

## 证据与限制
实际证据是本目录四个 checkpoint.json、result.md、duration.txt 和 results.json。执行者报告已读必要参考及做内存复现，但本评估者没有逐步工具 trace，不能独立把“按时读完全部 required references”和执行过程合规标记通过。时长是 agent 自报测量，不包含统一调度/排队边界，不用于速度优胜结论。token 计量不可得，全部为 null；没有费用估算，也没有事后成本阈值。只有一个极小 Python fixture、每臂两次、相同模型继承设置、无法完全排除工具/调度差异，不能推广可靠性或量化因果收益。

## 维护决策
不新增checkpoint强制规则：明确允许临时存储后四次均产出有效终态文件，尚未复现原先遗漏。保留现有核心行为，不宣称当前版更优。触发人工检查4/4，宿主路由未测。严格held-out、工具trace、可比成本仍未完成。原始路径为临时目录；本目录保留了报告与原始输出，checkpoint引用的原始路径可能随临时目录清理而失效。
