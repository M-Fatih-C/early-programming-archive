package com.example.saytahminetmeoyunu;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.EdgeEffect;
import android.widget.EditText;
import android.widget.TextView;

import java.util.Random;

public class MainActivity extends AppCompatActivity {

    private TextView txtKalanHak, txtSonuc;
    private EditText editTxtSayi;
    private String gelenDeger;
    private int kalanHak = 3, randomsayi;
    private Random rndSayi;
    private boolean tahminDogrumu = false;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        txtKalanHak = (TextView) findViewById(R.id.txtKalanHak);
        txtSonuc = (TextView) findViewById(R.id.txtViewSonuc);
        editTxtSayi = (EditText) findViewById(R.id.editTxtSayi);

        rndSayi = new Random();
        randomsayi = rndSayi.nextInt(10);
        System.out.println("Random Sayı : " + randomsayi);

    }

    public void btnTahminEt(View v) {
        gelenDeger = editTxtSayi.getText().toString();

        if (!TextUtils.isEmpty(gelenDeger)) {
            if (kalanHak > 0 && tahminDogrumu == false) {
                if (gelenDeger.equals(String.valueOf(randomsayi))){
                    sonucGoster("Tebrikler Doğru Tahmin Yaptınız!");
                    tahminDogrumu = true;
                }
                else {
                    txtSonuc.setText("Yanlış Tahmin Yaptınız! Tekrar Deneyin");
                    editTxtSayi.setText("");
                }
                kalanHak--;
                txtKalanHak.setText("Kalan Hak: " + kalanHak);

                if (kalanHak == 0 && tahminDogrumu == false){
                    sonucGoster("Tahmin Hakkınız Bitti!");
                    editTxtSayi.setText(" ");
                }
            } else
                txtSonuc.setText("Oyun Bitti!");
        } else
            txtSonuc.setText("Girilen Değer Boş Bırakılamaz!");
    }

    private void sonucGoster(String mesaj) {
        editTxtSayi.setEnabled(false);
        txtSonuc.setText(mesaj);
    }
}