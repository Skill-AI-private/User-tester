"""
UX Usability Reporter & System Usability Scale (SUS) Calculator.
"""
import os
import json
from datetime import datetime
from typing import Dict, List, Any


def calculate_sus_score(answers: List[int]) -> float:
    """
    Tính điểm System Usability Scale (SUS) chuẩn quốc tế từ 10 câu hỏi (thang 1-5).
    - Câu lẻ (1, 3, 5, 7, 9): Điểm = Giá trị - 1
    - Câu chẵn (2, 4, 6, 8, 10): Điểm = 5 - Giá trị
    Tổng điểm của 10 câu nhân với 2.5 sẽ ra thang điểm 100.
    """
    if len(answers) != 10:
        return 50.0  # Mặc định trung bình nếu thiếu dữ liệu
    
    score_sum = 0
    for i, ans in enumerate(answers):
        val = max(1, min(5, ans))
        if i % 2 == 0:  # Câu lẻ (0-indexed)
            score_sum += (val - 1)
        else:  # Câu chẵn
            score_sum += (5 - val)
            
    return round(score_sum * 2.5, 1)


def get_sus_grade(score: float) -> str:
    """Phân loại thang điểm SUS chuẩn quốc tế"""
    if score >= 80.3:
        return "Hạng A (Rất xuất sắc / Delighted)"
    elif score >= 68.0:
        return "Hạng B (Tốt / Đạt tiêu chuẩn thị trường)"
    elif score >= 51.0:
        return "Hạng C / D (Dưới trung bình / Cần cải tiến gấp)"
    else:
        return "Hạng F (Rất tệ / Người dùng dễ từ bỏ sản phẩm)"


def generate_markdown_report(
    session_data: Dict[str, Any],
    output_dir: str = "./reports"
) -> str:
    """Xuất báo cáo trải nghiệm người dùng định dạng Markdown chuyên nghiệp"""
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = os.path.join(output_dir, f"ux_report_{timestamp}.md")
    
    persona = session_data.get("persona", {})
    goal = session_data.get("goal", "Không xác định")
    start_url = session_data.get("start_url", "")
    steps = session_data.get("steps", [])
    sus_answers = session_data.get("sus_answers", [3] * 10)
    sus_score = calculate_sus_score(sus_answers)
    sus_grade = get_sus_grade(sus_score)
    final_feedback = session_data.get("final_feedback", {})

    content = f"""# 📊 Báo Cáo Kiểm Thử Trải Nghiệm Người Dùng (AI Usability Test Report)

- **Thời gian thực hiện:** {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
- **Trang web kiểm thử:** [{start_url}]({start_url})
- **Mục tiêu người dùng (User Goal):** `{goal}`
- **Hồ sơ đại diện (Persona):** **{persona.get('name', 'Ẩn danh')}** ({persona.get('age', 'N/A')} tuổi)
  - Trình độ công nghệ: *{persona.get('tech_literacy', 'Bình thường')}*
  - Đặc điểm thị giác: *{persona.get('vision_condition', 'Bình thường')}*
  - Mức độ kiên nhẫn: *{persona.get('patience_level', 'Trung bình')}*

---

## 🏆 1. Đánh Giá Khả Dụng Tổng Thể (System Usability Scale - SUS)

| Chỉ số | Điểm số | Đánh giá phân loại |
| :--- | :--- | :--- |
| **Điểm SUS chuẩn (0-100)** | **{sus_score}/100** | **{sus_grade}** |
| **Tổng số bước thao tác** | `{len(steps)} bước` | {'Hoàn thành suôn sẻ' if len(steps) <= 7 else 'Hơi mất nhiều thao tác'} |
| **Mức độ hài lòng chung** | `{final_feedback.get('overall_satisfaction', 7)}/10` | Dựa trên cảm nhận của Persona |

> 💡 *Điểm chuẩn trung bình toàn cầu cho các trang web hiện nay là 68/100. Điểm trên 80 được xem là trải nghiệm người dùng vượt trội.*

---

## 🚨 2. Các Điểm Gây Ức Chế / Ma Sát (Friction Points)

Những chi tiết giao diện làm AI bối rối, dừng lại hoặc không hiểu:

"""
    friction_found = False
    for i, step in enumerate(steps):
        friction = step.get("confusion_or_friction")
        severity = step.get("friction_severity", "none")
        if friction and severity != "none":
            friction_found = True
            badge = "🔴 Nghiêm trọng" if severity == "high" else ("🟡 Trung bình" if severity == "medium" else "🟢 Nhẹ")
            content += f"""### Bước {i+1}: {badge}
- **Ấn tượng ban đầu:** {step.get('visual_impression', '')}
- **Vấn đề gặp phải:** {friction}
- **Tác động:** Làm chậm quá trình người dùng hoàn thành mục tiêu.
"""

    if not friction_found:
        content += "_Không ghi nhận rào cản thao tác nào đáng kể trong suốt hành trình._\n"

    content += """
---

## 👣 3. Nhật Ký Hành Trình Trải Nghiệm (Think-Aloud Step-by-Step)

| Bước | AI nhìn thấy gì | Cảm nghĩ & Khó khăn | Hành động dự định làm | Điểm bước |
| :---: | :--- | :--- | :--- | :---: |
"""
    for i, step in enumerate(steps):
        what_see = ", ".join(step.get("what_i_see", []))
        friction = step.get("confusion_or_friction") or "Mượt mà, không vướng mắc"
        action = step.get("next_intended_action", {})
        action_desc = f"{action.get('action_type', '')}: {action.get('target_description', '')}"
        sat = step.get("satisfaction_at_step", 3)
        content += f"| **{i+1}** | {what_see} | {friction} | `{action_desc}` | {sat}/5 ⭐ |\n"

    content += f"""
---

## 💡 4. Đề Xuất Cải Thiện Giao Diện (Actionable UX Recommendations)

{final_feedback.get('recommendations_markdown', '''
1. **Tăng độ tương phản & cỡ chữ:** Đảm bảo các nhãn quan trọng và giá tiền dễ nhìn với người mắt kém hoặc người lớn tuổi.
2. **Làm nổi bật nút Kêu gọi hành động (Primary CTA):** Giữ nút mua hàng hoặc đăng ký luôn ở vị trí đập vào mắt trong vòng 3 giây đầu tiên.
3. **Giảm thiểu các bước trung gian:** Hạn chế pop-up chen ngang khi người dùng đang trên luồng thực hiện tác vụ chính.
''')}

---
*Báo cáo được khởi tạo tự động bởi framework **AI User-Tester (Synthetic Usability Engine)**.*
"""
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(content)
        
    return report_file
