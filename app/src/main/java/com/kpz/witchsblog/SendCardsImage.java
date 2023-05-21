package com.kpz.witchsblog;

import android.content.Context;
import android.util.Log;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import java.util.HashMap;
import java.util.Map;

public class SendCardsImage {
    public void SendImage(String base64Image, Context CardsRecognitionContext){
        RequestQueue queue = Volley.newRequestQueue(CardsRecognitionContext);
        String url ="http://192.168.1.17:5000/process";

        StringRequest stringRequest = new StringRequest(Request.Method.POST, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                //Toast.makeText(CardsRecognitionContext, error.getLocalizedMessage(), Toast.LENGTH_SHORT).show();
                Log.d("OnErrorResponse", "Time out!");
            }
        }){
            protected Map<String, String> getParams(){
                Map<String, String> paramV = new HashMap<>();
                paramV.put("image", base64Image);
                return paramV;
            }
        };
        queue.add(stringRequest);
    }
}
