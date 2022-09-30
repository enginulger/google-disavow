# Google Search Console Disavow 

Zararlı Backlinklerin Tespit Edilmesi

Disavow Tool kısaca; web sitesinden aldığınız linkin zararlı olduğunu ya da linkin tanınmadığı durumlarda ise bunu Google arama motoruna bildirmek için kullanabileceğiniz bir araçtır.

Python kullanarak zararlı linkleri bulup .txt dosyasında depolamak. Aşağıdaki 3. Adım ile Google arama motoruna bu zararlı linkleri bildirerek spamlı linklerden veya alan adlarından kurtuluyoruz.

Seo çalışmasında etkisi mevcuttur.

---

## 1. Adım - Edit Code
Kodu kendi domain bilgilerinize göre düzenleyin.

## 2. Adım - Setup
```
pip install virtualenv
virtualenv env
env\Scripts\activate
pip install -r requirements.txt
(env) python disavow.py
```
İlgili klasörde disavow.txt dosyası oluşuyor. 

---

## 3. Adım - Setting

Google Search Console Disavow:
https://search.google.com/search-console/disavow-links

Add or update disavow.txt

Google Search Console mülk eklerken yeni/eski seçeneği sunmaktadır. Bunlar;

yeni: exlample.com
eski: www.exlample.com

İki mülküde aynı hesaba ekleyebilirsiniz. 
Fakat Disavow kullanmak için eski seçenekli mülkü seçmeniz gerekmektedir.

---

## 4. Adım - Update

- disavow.txt bulunan spam domainler ortalama 1 ay içerisinde google tarafından kaldırılacaktır.
- disavow.txt her ay güncellemenizi tavsiye ederim.
- disavow.py dosyasını her ay çalıştırıp oluşan yeni disavow.txt Google Search Console bölümünden güncelleme yapabilirsiniz.

---

<div align="center">

<i>Other places you can find us:</i><br>

<a href="https://www.twitter.com/enginulger06" target="_blank"><img src="https://img.shields.io/badge/Twitter-%231877F2.svg?&style=flat-square&logo=twitter&logoColor=white" alt="Twitter"></a>

</div>