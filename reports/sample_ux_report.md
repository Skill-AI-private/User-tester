# 📊 Báo Cáo Kiểm Thử Trải Nghiệm Mẫu (Sample Usability Report)

- **Thời gian thực hiện:** 06/11/2026 11:30:00
- **Trang web kiểm thử:** [https://ecommerce-store-sample.com](https://ecommerce-store-sample.com)
- **Mục tiêu người dùng (User Goal):** `Tìm mua một chiếc áo sơ mi nam size L và thêm vào giỏ hàng`
- **Hồ sơ đại diện (Persona):** **Bác Ba (Người lớn tuổi)** (58 tuổi)
  - Trình độ công nghệ: *Thấp - Trung bình*
  - Đặc điểm thị giác: *Mắt kém, dễ mỏi, cần chữ to và độ tương phản cao*
  - Mức độ kiên nhẫn: *Thấp khi gặp lỗi hoặc từ ngữ công nghệ khó hiểu*

---

## 🏆 1. Đánh Giá Khả Dụng Tổng Thể (System Usability Scale - SUS)

| Chỉ số | Điểm số | Đánh giá phân loại |
| :--- | :--- | :--- |
| **Điểm SUS chuẩn (0-100)** | **52.5/100** | **Hạng C / D (Dưới trung bình / Cần cải tiến gấp)** |
| **Tổng số bước thao tác** | `5 bước` | Hơi mất nhiều thao tác |
| **Mức độ hài lòng chung** | `5/10` | Khá bối rối ở khâu chọn kích cỡ và pop-up |

> 💡 *Điểm chuẩn trung bình toàn cầu cho các trang web hiện nay là 68/100. Điểm dưới 60 là dấu hiệu rõ ràng cho thấy người dùng gặp nhiều rào cản nhận thức.*

---

## 🚨 2. Các Điểm Gây Ức Chế / Ma Sát (Friction Points)

Những chi tiết giao diện làm AI bối rối, dừng lại hoặc không hiểu:

### Bước 1: 🔴 Nghiêm trọng (Pop-up đập vào mắt)
- **Ấn tượng ban đầu:** Vừa vào trang thì bị một pop-up quảng cáo "Nhận voucher 20%" che toàn bộ màn hình.
- **Vấn đề gặp phải:** Dấu `X` để tắt pop-up có màu xám nhạt nằm sát góc trên bên phải, kích thước chỉ 12px nên rất khó nhìn thấy.
- **Tác động:** Người lớn tuổi sợ bấm nhầm hoặc nghĩ trang web bị lỗi.

### Bước 3: 🟡 Trung bình (Kích thước chữ chọn Size)
- **Ấn tượng ban đầu:** Đã vào được trang chi tiết áo sơ mi.
- **Vấn đề gặp phải:** Bảng chọn size S/M/L/XL chỉ là các ô vuông nhỏ màu xám không có nhãn giải thích số đo chiều cao/cân nặng tương ứng.
- **Tác động:** Người dùng phân vân không biết mình mặc vừa size nào, làm đứt đoạn quyết định mua.

---

## 👣 3. Nhật Ký Hành Trình Trải Nghiệm (Think-Aloud Step-by-Step)

| Bước | AI nhìn thấy gì | Cảm nghĩ & Khó khăn | Hành động dự định làm | Điểm bước |
| :---: | :--- | :--- | :--- | :---: |
| **1** | Pop-up quảng cáo che màn hình | Dấu X tắt pop-up quá mờ và nhỏ | `click: Nút đóng pop-up` | 2/5 ⭐ |
| **2** | Banner trang chủ, danh mục Áo nam | Chữ menu hơi nhỏ nhưng vẫn đọc được | `click: Danh mục Áo Nam` | 4/5 ⭐ |
| **3** | Danh sách sản phẩm dạng lưới | Hình ảnh rõ ràng, giá tiền dễ đọc | `click: Chọn Áo sơ mi trắng` | 5/5 ⭐ |
| **4** | Chi tiết áo, các ô chọn size S, M, L | Không biết bấm vào đâu để xem bảng size | `scroll: Cuộn tìm thông số` | 3/5 ⭐ |
| **5** | Nút "Thêm vào giỏ" màu xanh lá | Nút to, rõ ràng, dễ bấm | `click: Thêm vào giỏ` | 5/5 ⭐ |

---

## 💡 4. Đề Xuất Cải Thiện Giao Diện (Actionable UX Recommendations)

1. **Điều chỉnh Pop-up tiếp thị:** Trì hoãn việc hiện pop-up sau ít nhất 30 giây lướt web, làm nút đóng to tối thiểu 24x24px với độ tương phản cao.
2. **Thêm gợi ý Size thông minh:** Hiển thị rõ `Size L (65 - 75kg)` ngay trên nút chọn thay vì chỉ để mỗi chữ `L`.
3. **Tăng cường khả năng tiếp cận (Accessibility):** Tuân thủ tiêu chuẩn WCAG 2.1 AA với độ tương phản màu chữ đạt tối thiểu 4.5:1.
