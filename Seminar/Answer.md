1.So sánh greedy với backtracking? 
Greedy algorithm : Theo khái niệm greedy là thuật toán giải quyết một bài toán theo kiểu metaheuristic để tìm kiếm lựa chọn tối ưu địa phương ở mỗi bước đi với hy vọng tìm được tối ưu toàn cục.
Backtracking :  Một kĩ thuật thiết kế giải thuật dựa trên đệ quy. Ý tưởng của quay lui là tìm lời giải từng bước, mỗi bước chọn một trong số các lựa chọn khả dĩ và đệ quy
2.Tại sao trong ví dụ Knight không thể hiện backtracking ?
Trong ví dụ của bài báo cáo , video thể hiện quá trình giải bài Knight chạy nhanh nên khó để ý được lúc sử dụng kĩ thuật Backtracking .Vấn đề này đã được nói rõ ở trên lớp.
3.Meta-heuristic là gì?
các kỹ thuật dựa trên kinh nghiệm để giải quyết vấn đề, học hỏi hay khám phá nhằm đưa ra một giải pháp mà không được đảm bảo là tối ưu
4.Khi nào thì dùng backtracking?
Đã được bổ sung rõ trong sile số 10 trong Backtracking_update.pptx
5.Khía cạnh gì của bài toán thì có thể dùng backtracking 
Thông thường backtracking sẽ sử dụng khi bài toán có yêu cầu ràng buộc
6.Trong trường hợp nào thì thuật toán bt là tốt nhất?
Như câu 4
7. Phân biệt node promising và non promising?
Promising: Là node con tham gia vào việc tạo nên giải pháp ( nằm trên đường đi từ gốc một node lá – là giải pháp cho bài toán).
Ngược lại được gọi là non-promising
8.Hiện nay có thuật toán nào thay thế cho btk?
Backtracking không phải là thuật toán mà là một tư tưởng thiết kế thuật toán.
9.Ứng dụng thực tế dùng btk?
Lập trình game , giải các bài toán liên quan tới bản đồ ( tô màu đồ thị, tìm đường đi ngắn nhất ,...)
10.Làm sao ước lượng độ phức tạp của btk?
Tùy thuộc vào chiều cao của cây và quá trình tìm ra ứng viên phù hợp
11.Có thể dùng thuật toán nào thay thế cho bài Knight Tour?
Greedy tree 
