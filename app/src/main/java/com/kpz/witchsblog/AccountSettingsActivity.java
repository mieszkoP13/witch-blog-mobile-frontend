package com.kpz.witchsblog;

import static android.view.View.SYSTEM_UI_FLAG_FULLSCREEN;
import static android.view.View.SYSTEM_UI_FLAG_HIDE_NAVIGATION;
import static android.view.View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY;
import static android.view.View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN;
import static android.view.View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION;
import static android.view.View.SYSTEM_UI_FLAG_LAYOUT_STABLE;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Toast;

public class AccountSettingsActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().getDecorView().setSystemUiVisibility(SYSTEM_UI_FLAG_IMMERSIVE_STICKY | SYSTEM_UI_FLAG_HIDE_NAVIGATION   |
                SYSTEM_UI_FLAG_LAYOUT_STABLE | SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION | SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setContentView(R.layout.activity_register);

        setContentView(R.layout.activity_account_settings);
    }

    public void ChangeAvatarButton(View view) {
        Toast.makeText(this, "Zmień avatar użytkownika", Toast.LENGTH_SHORT).show();
    }
    public void ChangeBirthDateButton(View view) {
        Toast.makeText(this, "Zmień datę urodzenia", Toast.LENGTH_SHORT).show();
    }
    public void ChangeBirthTimeButton(View view) {
        Toast.makeText(this, "Zmień godzinę urodzenia", Toast.LENGTH_SHORT).show();
    }
    public void ChangeBirthCountryButton(View view) {
        Toast.makeText(this, "Zmień kraj urodzenia", Toast.LENGTH_SHORT).show();
    }
    public void ChangeBirthCityButton(View view) {
        Toast.makeText(this, "Zmień miasto urodzenia", Toast.LENGTH_SHORT).show();
    }
}