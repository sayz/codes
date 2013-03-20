package com.sayz.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class Kisi
 */
@WebServlet("/kisi")
public class KisiServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	Ogrenci ogr = new Ogrenci();
	Memur mem = new Memur();
	OgretimGorevlisi og = new OgretimGorevlisi();
	
	
    /**
     * @see HttpServlet#HttpServlet()
     */
    public KisiServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
    public void doGet(HttpServletRequest request,
            HttpServletResponse response)
            		throws ServletException, IOException {
    	response.setContentType("text/html");
    	response.setCharacterEncoding("UTF-8");
    	
    	/* Öğrenci sınıfı için test kısmı */
    	
    	
		ogr.setAd("İlknur");
		ogr.setSoyad("Karataş");
		ogr.setBolum("Tıp");
		ogr.setMemleket("Samsun");
		ogr.setSinif("5");
		ogr.setTcno(123);
		
		/*Memurlar için test kısmı*/
		mem.setAd("Ali Veli");
		mem.setSoyad("Selami");
		mem.setGorev("Ayakçı");
		mem.setTcno(12312312);
		mem.setMemNo(23456);
		
		/*Öğretim Görevlileri için test kısmı*/
		og.setAd("Recai");
		og.setSoyad("Oktaş");
		og.setDal("Bilgisayar Mühendisliği");
		og.setYas(45);
		og.setSicilNo("76457623547");
		og.setTcno(1237256);
		

    	PrintWriter out = response.getWriter();
    	String docType =
    			"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 " +
    			"Transitional//EN\">\n";
        String title = "Test";
		out.println ( docType +
        		"<HTML>\n" +
        		"<HEAD><TITLE>" + title  + "</TITLE></HEAD>\n" +
        		"<CENTER>\n" +
        		"<BODY BGCOLOR=\"#FDF5E6\">\n" +
        		"<H1>" + title + "</H1>\n");
        out.println(
        		"<h3>" + "Örenciler için test" + "</h3>" + "<br \\>" +
        		ogr.infoPer() + "<br \\>" +
        		ogr.infoOgr() + "<br \\>" +
        		ogr.getAd() + " " +ogr.gezer() + "<br \\>" +
        		ogr.getAd() + " " +ogr.uyur() + "<br \\>" +
        		ogr.getAd() + " " +ogr.kantin() + "<br \\><br \\>" +
        		"<h3>"+"Öğretim Görevlileri için test"+"</h3>" + "<br \\>" +
        		og.infoPer() + "<br \\>" +
        		og.getDal() + "<br \\>" +
        		og.getSicilNo() + "<br \\>" +
        		"Yaş: " + og.getYas() + "<br \\>" +
        		og.getAd() + " " + og.sınav() + "<br \\>" +
        		og.getAd() + " " + og.ders() + "<br \\><br \\>" +
        		"<h3>" + "Memurlar için test" + "</h3>" + "<br \\>" +
        		mem.infoPer() + "<br \\>" +
        		mem.infoMem() + "<br \\>" +
        		mem.getAd() +" "+ mem.evrakGotur() + "<br \\>"
        		);
        out.println("</BODY></HTML>");
              
        
    	
    }

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
	}

}
