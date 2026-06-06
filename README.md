# Vietnamese Fake News Dataset

Dataset phục vụ nghiên cứu bài toán **Phát hiện tin giả trong tiếng Việt**.

## Giới thiệu

Sự phát triển của mạng xã hội và các nền tảng truyền thông trực tuyến đã làm gia tăng tốc độ lan truyền thông tin. Bên cạnh những lợi ích tích cực, tin giả (fake news) và các nội dung sai lệch cũng xuất hiện ngày càng nhiều, đặc biệt trong các lĩnh vực như chính trị, chính sách công, kinh tế, giáo dục và đời sống xã hội.

Bộ dữ liệu này được xây dựng nhằm hỗ trợ nghiên cứu và phát triển các mô hình học máy, học sâu và mô hình ngôn ngữ lớn (LLM) cho bài toán phát hiện tin giả tiếng Việt.

---

## Thống kê dữ liệu

| Nhãn | Ý nghĩa              | Số lượng |
| ---- | -------------------- | -------: |
| 0    | Tin thật (Real News) |      734 |
| 1    | Tin giả (Fake News)  |     3638 |

Tổng số mẫu: **4372**

Dữ liệu có sự mất cân bằng giữa hai lớp, phản ánh đặc điểm thường gặp của dữ liệu thu thập từ môi trường thực tế.

---

## Cấu trúc dữ liệu

Mỗi bản ghi bao gồm:

| Trường    | Mô tả                 |
| --------- | --------------------- |
| `id`      | Mã định danh bài viết |
| `title`   | Tiêu đề bài viết      |
| `content` | Nội dung bài viết     |
| `label`   | Nhãn phân loại        |

Trong đó:

```text
0 = Real News
1 = Fake News
```

Ví dụ:

```json
{
  "id": 123,
  "title": "Chính phủ ban hành chính sách mới",
  "content": "...",
  "label": 0
}
```

---

## Chia tập dữ liệu

Dữ liệu được chia sẵn thành:

```text
dataset/
├── train.csv
├── validation.csv
└── test.csv
```

| Tập dữ liệu | Số lượng |
| ----------- | -------: |
| Train       |     3060 |
| Validation  |      656 |
| Test        |      656 |

Việc chia dữ liệu được thực hiện theo hướng duy trì phân phối nhãn tương đối đồng nhất giữa các tập.

---

## Tiền xử lý dữ liệu

Các bước tiền xử lý chính:

* Chuẩn hóa văn bản về chữ thường.
* Loại bỏ ký tự đặc biệt và nhiễu.
* Tách từ tiếng Việt bằng `underthesea`.
* Loại bỏ stopwords.
* Trích xuất các đặc trưng thống kê:

  * Số lượng từ.
  * Số lượng ký tự.
  * Số lượng dấu chấm than.
  * Mật độ tính từ.
* Biểu diễn văn bản bằng TF-IDF.

---

## Baseline Models

Các mô hình baseline được huấn luyện trên cùng bộ dữ liệu:

| Model               |   Accuracy |   F1-score |
| ------------------- | ---------: | ---------: |
| Naive Bayes         |     0.8399 |     0.7764 |
| Logistic Regression |     0.8567 |     0.8176 |
| Random Forest       |     0.8537 |     0.8168 |
| BiLSTM              |     0.8216 |     0.8213 |
| PhoBERT             |     0.8578 |     0.8375 |
| SVM                 | **0.8704** | **0.8490** |

Kết quả cho thấy SVM đạt hiệu năng tốt nhất trên bộ dữ liệu hiện tại.

---

## Ứng dụng

Dataset có thể được sử dụng cho:

* Fake News Detection.
* Text Classification.
* Vietnamese NLP.
* Benchmark cho các mô hình:

  * Machine Learning
  * Deep Learning
  * Transformer
  * Large Language Models (LLMs)

---

## Hướng phát triển

* Mở rộng quy mô dữ liệu.
* Cân bằng phân phối nhãn.
* Bổ sung dữ liệu từ mạng xã hội.
* Phát triển dữ liệu đa phương thức (Text + Image).
* Đánh giá các mô hình LLM hiện đại.
* Xây dựng hệ thống phát hiện tin giả theo thời gian thực.

---

