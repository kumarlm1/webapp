package com.example.myapplication;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Build;
import android.os.Bundle;
import android.provider.SyncStateContract;
import android.util.Log;
import android.view.View;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.Chronometer;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.parse.Parse;
import com.parse.ParseException;
import com.parse.ParseObject;
import com.parse.SaveCallback;

import org.json.JSONObject;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class MainActivity extends AppCompatActivity {
    EditText write;
    String data;
    TextView txt;
    Button btn,get,post;
    WebView webview;
    public  String TAG="dsvdvsdv";
    JSONObject file = new JSONObject();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        write=findViewById(R.id.write);
        txt=findViewById(R.id.txt);
        btn=findViewById(R.id.btn);
        get=findViewById(R.id.get);
        post=findViewById(R.id.post);

//        webview=findViewById(R.id.webview);
//        webview.setWebViewClient(new WebViewClient());
//        WebSettings webSettings=webview.getSettings();
//        webSettings.setJavaScriptEnabled(true);
//        webSettings.setAppCacheEnabled(true);
//        webview.loadUrl("http://ysyouthgct.social/");
//
        get.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.d(TAG, "onClick: entered");
                RequestQueue queue= Volley.newRequestQueue(MainActivity.this);
                String url="http://192.168.43.126:8000";
                StringRequest stringRequest=new StringRequest(Request.Method.GET, url, new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        Log.d("MainActivity", "onResponse: "+response);
                        txt.setText(response);
                    }
                }
                        , new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Log.d("Main activity", "onErrorResponse: "+error);
                    }
                });
                queue.add(stringRequest);
            }
        });

        post.setOnClickListener(new View.OnClickListener() {
            @RequiresApi(api = Build.VERSION_CODES.KITKAT)
            @Override
            public void onClick(View v) {
                Log.d(TAG, "onClick: entered");
                RequestQueue queue = Volley.newRequestQueue(MainActivity.this);
                String url = "http://192.168.43.126/";

                try {
                    file.put("username", "Ritu Sharma");
                    file.put("key", "Ritu password");
                    file.put("email", "ritu@gmail.com");
                    file.put("mobile", 88888888);

                } catch (Exception e) {
                }
                // Request a string response from the provided URL.
                StringRequest stringRequest = new StringRequest(Request.Method.POST, url,
                        new Response.Listener<String>() {
                            @Override
                            public void onResponse(String response) {
                                // your response
                                Log.d(TAG, "onResponse: "+response);

                            }
                        }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // error
                        Log.d(TAG, "onErrorResponse: "+error);
                    }
                }) {
                    @Override
                    public byte[] getBody() throws AuthFailureError {
                        String your_string_json = file.toString(); // put your json
                        return your_string_json.getBytes();
                    }
                };
                // Add the request to the RequestQueue.
                queue.add(stringRequest);



            }
        });


        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                data=write.getText().toString();
                FileOutputStream fo= null;
                try {
                    fo = openFileOutput("data",MODE_PRIVATE);
                    fo.write(data.getBytes());
                    fo.close();
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }

                Toast.makeText(getApplicationContext(),"added",Toast.LENGTH_LONG).show();
            }
        });




    }

    @Override
    public void onBackPressed() {
//        webview.goBack();
        super.onBackPressed();
    }
}
