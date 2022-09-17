# Xây dựng website bán hàng với Django

### Yêu cầu chức năng:
* Quản lý sản phẩm:
  * Trang quản trị: Danh sách, Thêm, sửa, xóa sản phẩm
  * Trang chủ hiển thị sản phẩm của shop
    * Thông tin của Product bao gồm:
      * Tên sản phẩm
      * Mã sản phẩm
      * Giá thành
      * Người tạo
      * Thời gian tạo
      * Thời gian update

    * Hiển thị danh sách sản phẩm với thông tin bao gồm:
      * Tên sản phẩm
      * Ảnh sản phẩm
      * Giá thành

      * Trang quản lý giỏ hàng
        * Thông tin Giỏ hàng bao gồm:
          * Sản phẩm (1 giỏ hàng có thể có nhiều Product – many-to-many)
          * Owner (Mỗi user chỉ có 1 giỏ hàng – one-to-one relation)
          * Thời gian tạo
          * Thời gian update
          * Tổng tiền của giỏ hàng

    * Trang thanh toán
      * Thông tin Giao dịch bao gồm:
        * Owner (Foreign key User – giao dịch này của ai)
        * Giỏ hàng (Foreign key – thanh toán cho giỏ hàng nào)
        * Tình trạng (Choice: Chưa thanh toán, Đã thanh toán)
        * Thời gian tạo
        * Thời gian update



* Quản lý người dùng:
  * Trang quản trị: Danh sách, Thêm, sửa, xóa người dùng
  * Đăng nhập, đăng ký, đăng xuất tài khoản