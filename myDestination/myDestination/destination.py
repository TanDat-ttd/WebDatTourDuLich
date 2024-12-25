from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")  # Tệp HTML phía trên sẽ được lưu là form.html

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    type_tour = request.form["type"]
    date = request.form["date"]
    tickets = request.form["tickets"]

    # Xử lý dữ liệu (ví dụ: lưu vào cơ sở dữ liệu hoặc gửi email xác nhận)
    response = f"""
    Đặt vé thành công!<br>
    Tên: {name}<br>
    Email: {email}<br>
    Số điện thoại: {phone}<br>
    Kiểu: {type_tour}<br>
    Ngày đi: {date}<br>
    Số lượng vé: {tickets}
    """
    return response

if __name__ == "__main__":
    app.run(debug=True)
