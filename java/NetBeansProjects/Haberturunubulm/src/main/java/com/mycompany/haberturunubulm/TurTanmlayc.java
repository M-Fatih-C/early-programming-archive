/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.haberturunubulm;

/**
 *
 * @author Muhammet Fatih
 */
import java.util.HashMap;
import java.util.Map;


public class TurTanımlayıcı {

    public TurTanımlayıcı(String articleTitle, String articleContent) {
    }
        public static void analyze(TurTanımlayıcı article, String[] keywords) {
            String articleContent = article.getContent().toLowerCase();
            int totalKeywordOccurrences = 0;

            Map<String, Integer> keywordCounts = new HashMap<>();

            for (String keyword : keywords) {
                int occurrences = 0;
                keyword = keyword.toLowerCase();

                // Using a simple loop to check for keyword occurrences
                for (int i = 0; i < articleContent.length() - keyword.length() + 1; i++) {
                    if (articleContent.substring(i, i + keyword.length()).equals(keyword)) {
                        occurrences++;
                    }
                }

                keywordCounts.put(keyword, occurrences);
                totalKeywordOccurrences += occurrences;
            }

            System.out.println("Title: " + article.getTitle());
            System.out.println("Total keyword occurrences: " + totalKeywordOccurrences);
            System.out.println("Keyword occurrences:");

            for (Map.Entry<String, Integer> entry : keywordCounts.entrySet()) {
                System.out.println("- " + entry.getKey() + ": " + entry.getValue());
        }
    }

    private String getTitle() {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }

    private Object getContent() {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }
    
}
