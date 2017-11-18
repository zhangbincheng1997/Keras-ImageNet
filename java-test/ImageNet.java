package com.redhat.bcml.util;

import java.io.File;
import java.util.Map;
import java.util.Set;

import org.apache.http.HttpEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.ContentType;
import org.apache.http.entity.mime.MultipartEntityBuilder;
import org.apache.http.entity.mime.content.FileBody;
import org.apache.http.entity.mime.content.StringBody;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.json.JSONObject;

public class ImageNet {

	private static String file = "D://dog.jpg";

	public static void main(String[] args) throws Exception {
		JSONObject jsonObj = uploadFileImpl(Consts.IMAGE_NET, file, "file", null);
		System.out.println(jsonObj.toString(2));
	}

	public static JSONObject uploadFileImpl(String serverUrl, String localFilePath, String serverFieldName,
			Map<String, String> params) throws Exception {
		String respStr = null;
		CloseableHttpClient httpclient = HttpClients.createDefault();
		try {
			HttpPost httppost = new HttpPost(serverUrl);
			FileBody binFileBody = new FileBody(new File(localFilePath));

			MultipartEntityBuilder multipartEntityBuilder = MultipartEntityBuilder.create();
			// add the file params
			multipartEntityBuilder.addPart(serverFieldName, binFileBody);
			// 设置上传的其他参数
			setUploadParams(multipartEntityBuilder, params);

			HttpEntity reqEntity = multipartEntityBuilder.build();
			httppost.setEntity(reqEntity);

			CloseableHttpResponse response = httpclient.execute(httppost);
			try {
				HttpEntity resEntity = response.getEntity();
				respStr = EntityUtils.toString(resEntity);
				EntityUtils.consume(resEntity);
			} finally {
				response.close();
			}
		} finally {
			httpclient.close();
		}
		return new JSONObject(respStr);
	}

	private static void setUploadParams(MultipartEntityBuilder multipartEntityBuilder, Map<String, String> params) {
		if (params != null && params.size() > 0) {
			Set<String> keys = params.keySet();
			for (String key : keys) {
				multipartEntityBuilder.addPart(key, new StringBody(params.get(key), ContentType.TEXT_PLAIN));
			}
		}
	}
}
