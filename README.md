chay bash: curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.0/docker-compose.yaml'
--> Lệnh này sẽ tải về file docker-compose.yaml — file dùng để tạo toàn bộ Airflow (webserver, scheduler, database…).

mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env

Thao tác này:   mkdir -p ./dags ./logs ./plugins
                echo -e "AIRFLOW_UID=$(id -u)" > .env


Tạo thư mục chứa DAGs

Tạo thư mục chứa logs

Tạo file .env để Airflow chạy đúng quyền
### level 1
    1️⃣ Tạo nhiều task trong DAG
    2️⃣ Tạo dependency giữa các task ( >> và << )
    3️⃣ Dùng PythonOperator
    4️⃣ Xem log + chạy thử

### level 2
    ✔ Chạy Python trong Airflow
    ✔ Dùng return để gửi dữ liệu qua XCom
    ✔ ti.xcom_pull() để lấy dữ liệu
    ✔ Chạy 2 task theo thứ tự# airflow
## level 2.2
    LEVEL 2.2 – XCom nâng cao

    Trong bài này bạn sẽ học:

        Truyền nhiều dữ liệu giữa task bằng XCom

        Dùng list, dict

        Task A → Task B → Task C chia nhỏ dữ liệu

        Rất giống ETL thực tế!
