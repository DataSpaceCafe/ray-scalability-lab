# Ray Data Cleaning Workshop

## ไฟล์ที่ใช้ในการ Workshop
1. **data_raw.csv** - ข้อมูลดิบที่มีปัญหา
2. **workshop-data-cleaning.py** - โค้ดสำหรับทำความสะอาดข้อมูล

## ปัญหาที่มีในข้อมูล
- ❌ Missing values (name, age, email, department, join_date)
- ❌ Invalid age (อายุติดลบ, มากกว่า 120)
- ❌ Invalid salary (เงินเดือนติดลบ)
- ❌ Invalid email format
- ❌ Invalid phone format

## ขั้นตอนการ Data Cleaning

### STEP 1: โหลดข้อมูล
- อ่านไฟล์ CSV ด้วย Ray Data
- ตรวจสอบจำนวน records และ schema

### STEP 2: ตรวจสอบปัญหา
- หา missing values ในแต่ละ column
- หาค่าที่ผิดปกติ (invalid age, salary)

### STEP 3: ทำความสะอาดข้อมูล (Parallel Processing)
- ลบ records ที่ไม่มีชื่อ
- แก้ไข age ที่ผิดปกติ → set เป็น None
- แก้ไข salary ที่ติดลบ → set เป็น None
- ตรวจสอบ email format
- ตรวจสอบ phone format
- กำหนดค่า default สำหรับ department

### STEP 4: เติมข้อมูลที่ขาดหาย
- คำนวณค่าเฉลี่ยของ age และ salary
- เติมค่าเฉลี่ยในช่องที่ว่าง

### STEP 5: แสดงผลลัพธ์
- แสดงข้อมูลที่สะอาดแล้ว
- คำนวณสถิติ
- จัดกลุ่มตาม department

### STEP 6: บันทึกข้อมูล
- บันทึกข้อมูลที่สะอาดแล้วเป็นไฟล์ CSV

## วิธีการรัน
```powershell
.\python-3.11.9-embed-amd64\python.exe .\workshop-data-cleaning.py
```

## ผลลัพธ์ที่ได้
- ไฟล์ **data_cleaned.csv** - ข้อมูลที่ทำความสะอาดแล้ว
- สถิติและสรุปข้อมูล
- Log เวลาของแต่ละขั้นตอน

## จุดเด่นของ Ray Data
✅ **Parallel Processing** - ประมวลผลหลาย records พร้อมกัน
✅ **Scalable** - รองรับข้อมูลขนาดใหญ่
✅ **Easy to use** - API ใช้งานง่ายคล้าย Pandas
✅ **Distributed** - กระจายงานไปหลาย CPU cores
