# Create the homepage (index.html)
index_content = """---
layout: default
title: Acasă
description: Laura Gheorghica - Consilier relațional cu peste 13 ani de experiență. Îți ofer un spațiu sigur pentru a învăța să construiești relații sănătoase și împlinite.
---

<section class="hero">
    <div class="container">
        <h1>Bună, sunt Laura Gheorghica</h1>
        <p>Consilier relațional cu peste 13 ani de experiență în comunicarea publică și managementul relațiilor. Îți ofer un spațiu sigur pentru a învăța să construiești relații sănătoase și împlinite.</p>
        <a href="{{ '/contact/' | relative_url }}" class="cta-button">Să vorbim</a>
    </div>
</section>

<section class="services-section">
    <div class="container">
        <h2 class="text-center mb-2">Cum te pot ajuta</h2>
        
        <div class="services-grid">
            <div class="service-card">
                <div class="service-icon">
                    <i class="fas fa-heart"></i>
                </div>
                <h3>Consiliere Relațională</h3>
                <p>Învață să construiești relații autentice și sănătoase. Explorăm împreună dinamica relațiilor, comunicarea eficientă și gestionarea conflictelor.</p>
            </div>
            
            <div class="service-card">
                <div class="service-icon">
                    <i class="fas fa-users"></i>
                </div>
                <h3>Terapie de Cuplu</h3>
                <p>Îți ofer instrumentele necesare pentru a-ți aprofunda relația de cuplu, a învăța să comunici autentic și a transforma conflictele în oportunități de creștere.</p>
            </div>
            
            <div class="service-card">
                <div class="service-icon">
                    <i class="fas fa-lightbulb"></i>
                </div>
                <h3>Programe de Dezvoltare</h3>
                <p>Programul "ABC-ul Relațiilor Fericite" și alte programe structurate care te ajută să înțelegi și să îmbunătățești calitatea relațiilor tale.</p>
            </div>
        </div>
    </div>
</section>

<section class="about-section">
    <div class="container">
        <div class="about-content">
            <div class="about-text">
                <h2>Despre mine</h2>
                <p>Sunt Laura Gheorghica, consilier relațional cu peste 13 ani de experiență în comunicarea publică și managementul relațiilor. Pasiunea mea este să ajut oamenii să construiască relații autentice și împlinite.</p>
                
                <p>Am observat că multe dintre problemele pe care le întâmpinăm în relații pot fi rezolvate prin înțelegerea dinamicii relaționale și dezvoltarea abilităților de comunicare. Cred că fiecare persoană merită să trăiască în relații sănătoase și pline de iubire.</p>
                
                <p class="quote">"Dacă lipsește ținta, viața e o rătăcire." - Seneca</p>
                
                <p>Această citație care îmi ghidează activitatea subliniază importanța direcției clare în relațiile noastre. Îți ofer un spațiu sigur unde să explorezi și să îți definești propriile obiective relaționale.</p>
                
                <a href="{{ '/despre/' | relative_url }}" class="cta-button">Află mai multe</a>
            </div>
            
            <div class="about-image">
                <!-- Placeholder for profile image -->
                <div style="width: 300px; height: 300px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto;">
                    <i class="fas fa-user" style="font-size: 100px; color: white; opacity: 0.7;"></i>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="cta-section" style="background: #f8f9fa; padding: 3rem 0;">
    <div class="container text-center">
        <h2>Să începem împreună o călătorie către relații mai sănătoase</h2>
        <p>Îți ofer un spațiu sigur și confidențial unde să explorezi și să îți dezvolți abilitățile relaționale.</p>
        <a href="{{ '/contact/' | relative_url }}" class="cta-button">Programează o consultație</a>
    </div>
</section>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)
    
print("Created index.html")