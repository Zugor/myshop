# Xây dựng website bán hàng với Django

Tài liệu về Django: https://docs.djangoproject.com/en/4.1/

Slide bài giảng: https://drive.google.com/drive/folders/1qHLWc0v8LA4BO9wpwBy3DsIrlQh7zm5A?usp=sharing

Template sử dụng để làm giao diện: https://demo.themesberg.com/pixel-bootstrap-5-ui-kit/#components


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


## Các câu lệnh cần nhớ
````
#Install django lib
pip3 install django

#Create django project
django-admin startproject project_name

#Create a App in the project
python manage.py startapp app_name

#Run server to access your website http://127.0.0.1:8000
python manage.py runserver

#Apply changes of a model
python manage.py makemigrations app_name
python manage.py migrate

#Create super user to login Admin page
python manage.py createsuperuser
````
