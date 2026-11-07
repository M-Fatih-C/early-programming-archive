package com.example.kitaplambas;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.provider.Settings;
import android.view.View;
import android.widget.ImageView;

public class MainActivity extends AppCompatActivity {

    ImageView ImageView;
    int deger = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ImageView = findViewById(R.id.ampul);

        izin(this);

        Settings.System.putInt(getContentResolver(),Settings.System.SCREEN_BRIGHTNESS,0);

        ImageView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(deger == 0 )
                {
                Settings.System.putInt(getContentResolver(),Settings.System.SCREEN_BRIGHTNESS,255);
                deger = 1;
                }else{
                    Settings.System.putInt(getContentResolver(),Settings.System.SCREEN_BRIGHTNESS,0);
                    deger = 0;
                }
            }
        });


    }


    public void izin(Context c){

        if(Settings.System.canWrite(c)){


        }else{
            Intent i = new Intent(Settings.ACTION_MANAGE_WRITE_SETTINGS);
            startActivity(i);
        }

    }
}