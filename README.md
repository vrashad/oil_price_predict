#  XGBoost vasitəsilə neftin gələcək qiymətinin proqnozlaşdırılması layihəsi 

Zaman sıralarının proqnozlaşdırılması, hər hansısa bir məlumatın zaman ardıcıllığı ilə proqnozlaşdırılması texnikasıdır. 

Bu texnika, keçmişin tendensiyalarını təhlil edərək gələcək məlumatları proqnozlaşdırır və gələcək tendensiyaların tarixi tendensiyalara oxşar olacağını güman edir.

Zaman sıralarının proqnozlaşdırılması vasitəsilə, gələcək tarixdəki neftin qiymətini proqnozlaşdırmaq üçün, bizə ilk olaraq keçmiş tarixdəki qiymətlər lazımdır.

Məlumatı biz buradan əldə edəcəyik https://finance.yahoo.com/quote/CL%3DF/history?p=CL%3DF

Bunun üçün **data_downloader.py** skriptini icra etmək lazımdır.

Skript avtomatik olaraq ona daxil edilən tarix çərçivəsindəki məlumatları əldə edərək, onu CSV faylında local yaddaşa yazır.


```bash
data = pdr.get_data_yahoo("CL=F", start="2000-01-01", end="2024-01-06")
```
Adından da göründüyü kimi **start** məlumatların başlanğıc tarixidir **end** isə son

Buradakı **CL=F** finance.yahoo da xam neftin adıdır

Skript icra edildikdən sonra **dataset.csv** faylı tərtib edilərək, 24 il ərzində neftin gündəlik qiymətləri fayla yazılacaq.

Cədvəl iki sütundan ibarət olacaq

**Date**: tarix<br>
**Adj Close**: həmin tarixdəki neftin qiyməti

 Dataset hazır olandan sonra **Oil_price_predict_xgboost.ipynb** Jupyter Notebook faylını ya local olaraq ya da Google Colab kimi Cloud servislərinin birində açırıq

 İlk olaraq **dataset.csv** faylını DataFrame çeviririk və matplotlib.pyplot vasitəsilə neftin keçmiş qiymət qrafikini ekrana çıxardırıq

<img src="https://i.postimg.cc/PfpCNJ94/1.png">

 Vizual olaraq görününr ki, neftin qiymətinin dəyişməsində tendensiya müşahidə olunur


Sonra əldə edəcəyimiz modelin dəqiqliyini yoxlamaq üçün, keçmiş qiymətləri Test və Təlim dəsti olaraq iki yerə bölürük

<img src="https://i.postimg.cc/MHCMKJzq/2.png">


Sonra müxtəlif vaxt seriyası məlumat dəstlərinin ardıcıl təlim və test dəstlərinə bölmək yolu ilə zamanla necə dəyişdiyini vizuallaşdırırıq

<img src="https://i.postimg.cc/T3RNJK88/3.png">


 
