Bài 1: Python là ngôn ngữ thông dịch vì:

Trước hết ta phải hiểu ngôn ngữ biên dịch là gì? Ngôn ngữ biên dịch là ngôn ngữ mà mã nguồn sẽ được dịch sang mã máy bởi trình biên dịch, sau đó máy tính sẽ thực hiện các lệnh theo file mã máy nhận được. Trong khi đó, ngôn ngữ thông dịch là từng dòng lệnh của mã nguồn sẽ được trình thông dịch thực hiện ngay tức thời mà không cần phải dịch trước cả file mã nguồn. VD: Việc dịch một buổi phỏng vấn, người phiên dịch sẽ dịch từng câu thay vì nghe hết cả đoạn văn rồi mới dịch lại tất cả.
Python không yêu cầu bước biên dịch trước khi chạy chương trình. Bạn có thể viết và chạy mã Python trực tiếp mà không cần lo lắng về việc biên dịch.
Python đi kèm với một Interactive Prompt, cho phép bạn tương tác trục tiếp với máy tính để thực hiện các câu lệnh.
Trong khi đó các ngôn ngữ biên dịch như C++ muốn chạy được trên máy tính thì phải trải qua một chương trình biên dịch để chuyển đổi từ dạng mã nguồn sang mã thực thi.


Bài 2: Các kiểu dữ liệu trong Python

int: đây là kiểu dữ liệu được sử dụng để lưu trữ các số nguyên (1, 2, 3, 4, ...). float: đây là kiểu dữ liệu dùng để lưu trữ các biến số kiểu thực (1.43, 5.34, 3.333, ...). bool: đây là kiểu dữ liệu dùng để lưu trữ các giá trị luận lý (True hoặc False) str: đây là kiểu dữ liệu dùng để lưu trữ các ký tự ("Viet Nam",...) Ngoài Python còn lại một số kiểu dữ liệu khác như list, set, dict, tuple, complex
Các toán tử trong Python

(+) Toán tử cộng 2 giá trị.
(-) Toán tử trừ 2 giá trị.
(*) Toán tử nhân 2 giá trị.
(/) Toán tử chia 2 giá trị.
(//) Toán tử chia lấy phần nguyên của 2 giá trị.
(%) Toán tử chia phần dư của 2 giá trị.
( ) Toán tử mũ (a b = ab)
Mệnh đề và vòng lặp trong Python

Câu lệnh If Cú pháp 1, if (biểu thức): 2, các câu lệnh Câu lệnh if kiểm tra xem biểu thức mang giá trị True hay False, nếu true thì thực hiện các câu lệnh.

Câu lệnh If..elif..else Cú pháp 1, if (biểu thức 1): 2, các câu lệnh 3, elif (biểu thức 2): 4, các câu lệnh 5, elif (biểu thức n): 6, các câu lệnh 7, else: 8, các câu lệnh Nếu bạn có nhiều trường hợp cần xử lý, chẳng hạn như tìm thử nghiệm phương trình bậc 2 có tới 3 trường hợp của delta, thì bạn sử dụng cú pháp if..elif..else.

Vòng lặp while Thường được sử dụng khi bạn chưa biết trước số lượng vòng lặp cần sử dụng. Cú pháp 1, while (biểu thức): 2, các câu lệnh Ý nghĩa của câu lệnh này là trong khi điều kiện còn đúng thì thực hiện các câu lệnh.

Vòng lặp thường được sử dụng khi bạn đã biết trước số lượng vòng lặp cần thực hiện. Cú pháp 1, for <biến lặp> in <tập hợp>: 2, ​​các câu lệnh Biến lặp có thể là bất kỳ biến nào. Bạn chỉ cần nhập vào một cái tên là Python sẽ tự động ngầm hiểu kiểu dữ liệu. Có tập hợp có thể là bất kỳ loại tập hợp nào hoặc cũng có thể là một chuỗi.

Câu lệnh Break Khi bạn muốn dừng vòng lặp giữa chừng thì dùng câu lệnh break.

Câu lệnh Continue Câu lệnh continue có tác dụng nhảy sang lặp lại tiếp theo. Các lệnh phía sau contine sẽ không thể thực hiện được.

Kiểu dữ liệu True, False Boolean là một kiểu dữ liệu mà các ngôn ngữ lập trình này thường xuyên sử dụng. Python cũng không ngoại lệ. Kiểu dữ liệu này chỉ có hai giá trị: + True – có nghĩa là đúng + False – có nghĩa là sai.