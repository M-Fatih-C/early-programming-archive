/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.haberturunubulm;

/**
 *
 * @author Muhammet Fatih
 */
public class Main {
    public static void main(String[] args) {
        String articleTitle = "Sample News Article";
        String articleContent = "This is a sample news article about Java programming. Java is a popular programming language.";

        TurTanımlayıcı article = new TurTanımlayıcı(articleTitle, articleContent);

        String[] keywords = {"java", "programming"};

        NewsArticleAnalyzer.analyze(article, keywords);
    }
}