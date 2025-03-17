# 📋 TaskMaster Bot

TaskMaster Bot, Discord üzerinde görev ekleme, silme, tamamlama ve listeleme işlemlerini kolaylaştıran bir görev yönetim botudur. Bu bot, kullanıcıların görevlerini organize etmelerine yardımcı olur ve SQLite kullanarak görevleri kalıcı olarak saklar.

## 🚀 Özellikler

- ✅ **Görev Ekleme**: Yeni görevler tanımlayın.
- 🗑️ **Görev Silme**: Belirtilen görevleri kaldırın.
- 📊 **Görev Listeleme**: Tüm görevlerinizi görüntüleyin.
- ✔️ **Görev Tamamlama**: Görevlerinizi tamamlanmış olarak işaretleyin.

## 📂 Proje Yapısı

```
📦 task_manager_bot
├── 📄 bot.py                # Discord bot ana dosyası
├── 📄 database.py           # SQLite görev veritabanı işlemleri
└── 📄 requirements.txt      # Gerekli bağımlılıklar
```

## 🛠️ Kurulum

Bu projeyi kendi sisteminizde çalıştırmak için aşağıdaki adımları takip edin:

### 1. Depoyu Klonlayın

```bash
git clone https://github.com/AlgiMerve/discord_task_bot.git
cd discord_task_bot
```

### 2. Sanal Ortam (İsteğe Bağlı)

```bash
python -m venv venv
source venv/bin/activate  # Windows için: .\venv\Scripts\activate
```

### 3. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### 4. Botu Çalıştırın

`bot.py` dosyasındaki **TOKEN** kısmına kendi Discord bot token'ınızı ekleyin:

```python
bot.run('YOUR_DISCORD_BOT_TOKEN')
```

Ardından terminalde çalıştırın:

```bash
python bot.py
```

## 📖 Komutlar

| Komut              | Açıklama                            |
|--------------------|------------------------------------|
| `!add_task <açıklama>`   | Yeni bir görev ekler.               |
| `!delete_task <id>`      | Belirtilen ID'ye sahip görevi siler.|
| `!show_tasks`            | Tüm görevleri listeler.             |
| `!complete_task <id>`    | Görevi tamamlanmış olarak işaretler.|

## 🧰 Geliştirici Notları

- Discord API için `discord.py` kütüphanesi kullanıldı.
- Görevler `SQLite` veritabanında saklanır.
- Yeni özellikler için Pull Request gönderebilirsiniz.

## 🤝 Katkıda Bulunma

Katkıda bulunmak istiyorsanız lütfen bir **fork** alın, geliştirmelerinizi yapın ve **pull request** oluşturun.

## 📜 Lisans

Bu proje MIT lisansı altında sunulmaktadır.

---

💡 **Herhangi bir sorunuz olursa çekinmeden iletişime geçin!**
