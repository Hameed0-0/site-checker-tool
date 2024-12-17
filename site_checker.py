import requests
from bs4 import BeautifulSoup
import json
from fpdf import FPDF

# وظيفة لفحص الموقع وجلب الأخطاء
def check_site(url):
    errors = []

    try:
        # إرسال طلب GET
        response = requests.get(url)
        status_code = response.status_code
        
        if status_code != 200:
            errors.append(f"الموقع لا يعمل بشكل صحيح، رمز الحالة: {status_code}")
        else:
            print("[+] الموقع يعمل بنجاح")

        # استخدام BeautifulSoup لتحليل HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # فحص الروابط المكسورة
        links = soup.find_all('a', href=True)
        for link in links:
            link_url = link['href']
            try:
                if link_url.startswith("http"):
                    r = requests.get(link_url)
                    if r.status_code != 200:
                        errors.append(f"رابط مكسور: {link_url} (رمز الحالة: {r.status_code})")
            except:
                errors.append(f"فشل الوصول إلى الرابط: {link_url}")

    except Exception as e:
        errors.append(f"خطأ أثناء فحص الموقع: {e}")
    
    return errors

# وظيفة لإنشاء تقرير PDF
def generate_pdf_report(errors, filename="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="تقرير فحص الموقع", ln=True, align="C")
    pdf.ln(10)

    if not errors:
        pdf.cell(200, 10, txt="لم يتم العثور على أي أخطاء!", ln=True)
    else:
        for error in errors:
            pdf.multi_cell(0, 10, txt=error)

    pdf.output(filename)
    print(f"[+] تم إنشاء التقرير PDF: {filename}")

# وظيفة لإنشاء تقرير JSON
def generate_json_report(errors, filename="report.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump({"errors": errors}, f, ensure_ascii=False, indent=4)
    print(f"[+] تم إنشاء التقرير JSON: {filename}")

# نقطة تشغيل البرنامج
if __name__ == "__main__":
    print("أداة فحص المواقع - Site Checker")
    target_url = input("أدخل رابط الموقع لفحصه: ").strip()
    
    print(f"[*] جاري فحص الموقع: {target_url}")
    site_errors = check_site(target_url)

    # عرض النتائج
    if site_errors:
        print("\n[-] تم العثور على الأخطاء التالية:")
        for error in site_errors:
            print(f"   - {error}")
    else:
        print("\n[+] لم يتم العثور على أي أخطاء!")
    
    # إنشاء التقارير
    generate_pdf_report(site_errors)
    generate_json_report(site_errors)
