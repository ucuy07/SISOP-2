1. Sudah dijalankan selama 5 kali percobaan.
2. Dengan hasil catatan nilai counter 1: 200000, 2:200000, 3:200000, 4:200000, 5:200000.
3. Kalo dilihat dari hasil diatas tidak terjadi inkonsistensi, bisa jadi karena python memiliki mekanisme Global Interpreter Lock pada implementasinya, namun bisa terjadi inkonsistensi kalo dijalankan dengan sistem operasi yg lain atau perangkat lain.
4. Interleaving yang terjadi dengan counter 1 terlihat seperti 1 langkah, sebetulnya CPU menjalankannya dalam 3 langkah: baca → tambah → tulis. Jadi ada 3 langkah atau proses yg berjalan.