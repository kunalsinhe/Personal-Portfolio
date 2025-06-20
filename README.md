# Portfolio{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>About Me - Kunal Sinha</title>

  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href=" {% static "css/style.css" %}" />
  <script defer src="script.js"></script>
  
</head>
<body>
  <div class="container">
    <aside class="sidebar">
      <div class="avatar-box">
        <img src="avatar.png" alt="Kunal Sinha" class="avatar" />
      </div>
      <h2 class="name">Kunal Sinha</h2>
      <div class="role-label">Web Developer</div>
      <hr class="separator">
      <div class="contact-card">
        <div class="contact-item">
          <span class="icon">📧</span>
          <div class="contact-info">
            <span class="label">EMAIL</span>
            <span class="value">kunal@example.com</span>
          </div>
        </div>
        <div class="contact-item">
          <span class="icon">📞</span>
          <div class="contact-info">
            <span class="label">PHONE</span>
            <span class="value">+91-9876543210</span>
          </div>
        </div>
      </div>
    </aside>

    <main class="main-content">
      <nav class="navbar">
        <a class="nav-link active" href="#">About</a>
        <a class="nav-link" href="#">Resume</a>
        <a class="nav-link" href="#">Portfolio</a>
        <a class="nav-link" href="#">Blog</a>
        <a class="nav-link" href="#">Contact</a>
      </nav>

      <section class="about">
        <h1>About Me</h1>
        <hr class="separator">
        <p>
          I'm a passionate Web Developer and Tech Enthusiast from Nagpur, India. I enjoy creating modern, clean, and intuitive digital experiences.
          My focus is on building functional and visually appealing websites. I integrate AI and modern tools into solutions for educational and professional communities.
        </p>

        <h2>What I'm Doing</h2>
        <div class="cards">
          <div class="card">
            <h3>Web Design</h3>
            <p>Modern, responsive and high-quality UI/UX design made at a professional level.</p>
          </div>
          <div class="card">
            <h3>Web Development</h3>
            <p>Robust development of websites using HTML, CSS, JS and backend integration.</p>
          </div>
        </div>
      </section>
    </main>
  </div>
</body>
</html>

