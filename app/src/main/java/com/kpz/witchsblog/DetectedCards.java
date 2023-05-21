package com.kpz.witchsblog;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

public class DetectedCards extends AppCompatActivity {

    private TextView detectedCards;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detected_cards);
        detectedCards = (TextView) findViewById(R.id.detectedCardsTextView);
        //Bundle extras = getIntent().getExtras();
        //String data = extras.getString("data");
        //detectedCards.setText(data);
    }
}