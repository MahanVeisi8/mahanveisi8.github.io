---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
published: true
---

<!-- ===== Overall GitHub Stats header ===== -->
<section class="github-summary">
  <div class="github-summary__card">
    <h2 class="github-summary__title">Mahan Veisi's GitHub Stats</h2>
    <div class="github-summary__imgwrap">
      <img
        src="https://github-readme-stats.vercel.app/api?username=MahanVeisi8&show_icons=true&theme=transparent&rank_icon=github"
        alt="Mahan Veisi GitHub stats"
        loading="lazy"
      />
    </div>
  </div>

  <div class="github-summary__card">
    <h2 class="github-summary__title">Top Languages</h2>
    <div class="github-summary__imgwrap">
      <img
        src="https://github-readme-stats.vercel.app/api/top-langs/?username=MahanVeisi8&layout=compact&theme=transparent"
        alt="Top languages"
        loading="lazy"
      />
    </div>
  </div>
</section>


<!-- ===== Project Cards ===== -->
<section class="project-grid">

  <!-- Latent Diffusion MNIST -->
  <article class="project-card project-card--triple">

    <header class="project-card__titlebar">
      <h3 class="project-title">Latent Diffusion Models for MNIST</h3>
    </header>

    <figure class="project-media">
      <img
        src="/assets/img/projects/grid_diffusion_gif.gif"
        alt="Latent Diffusion MNIST"
      />
    </figure>

    <div class="project-body">
      <p class="project-desc">
        Built an unconditional latent diffusion model on MNIST.
      </p>
      <ul class="project-list">
        <li>Autoencoders + Channel Attention Blocks</li>
        <li>U-Net DDPM for denoising in latent space</li>
        <li>t-SNE embeddings &amp; reconstruction quality</li>
      </ul>
    </div>

    <aside class="project-meta">
      <div class="repo-embed">

        <a class="repo-embed__cardlink"
           href="https://github.com/MahanVeisi8/Latent-Diffusion-MNIST-DDPM-using-Autoencoder">
          <div class="repo-embed__cardimg">
            <img
              src="https://github-readme-stats.vercel.app/api/pin/?username=MahanVeisi8&repo=Latent-Diffusion-MNIST-DDPM-using-Autoencoder&theme=transparent&show_owner=true"
              alt="Latent Diffusion repo card"
              loading="lazy"
            />
          </div>
        </a>

        <a class="repo-embed__btn"
           href="https://github.com/MahanVeisi8/Latent-Diffusion-MNIST-DDPM-using-Autoencoder">
          <i class="fab fa-github"></i>
          View Repo
        </a>

      </div>
    </aside>

  </article>


  <!-- Rock–Paper–Scissors YOLOv11 -->
  <article class="project-card project-card--triple">

    <header class="project-card__titlebar">
      <h3 class="project-title">Rock–Paper–Scissors Game Automation with YOLOv11</h3>
    </header>

    <figure class="project-media">
      <img
        src="/assets/img/projects/rock-paper-scissors-yolov11.gif"
        alt="Rock–Paper–Scissors Game Automation with YOLOv11"
      />
    </figure>

    <div class="project-body">
      <p class="project-desc">
        Real-time hand-gesture detection powering a fully automated game with cheating detection and dynamic winner celebration.
      </p>
      <ul class="project-list">
        <li>YOLOv11 gestures at ~98.2% mAP@0.5</li>
        <li>Cheating detection: red mask &amp; −1 penalty</li>
        <li>Winner recognition: animated crown overlay</li>
      </ul>
    </div>

    <aside class="project-meta">
      <div class="repo-embed">

        <a class="repo-embed__cardlink"
           href="https://github.com/SBUformers/Rock-Paper-Scissors-Simulator">
          <div class="repo-embed__cardimg">
            <img
              src="https://github-readme-stats.vercel.app/api/pin/?username=SBUformers&repo=Rock-Paper-Scissors-Simulator&theme=transparent&show_owner=true"
              alt="Rock Paper Scissors repo card"
              loading="lazy"
            />
          </div>
        </a>

        <a class="repo-embed__btn"
           href="https://github.com/SBUformers/Rock-Paper-Scissors-Simulator">
          <i class="fab fa-github"></i>
          View Repo
        </a>

        <a class="repo-embed__btn"
           href="https://github.com/SBUformers/Rock-Paper-Scissors-Simulator/blob/main/Final_report.pdf">
          <i class="far fa-file-pdf"></i>
          Report
        </a>

      </div>
    </aside>

  </article>


  <!-- VAE MNIST -->
  <article class="project-card project-card--triple">

    <header class="project-card__titlebar">
      <h3 class="project-title">VAE for MNIST: Exploring Latent Spaces</h3>
    </header>

    <figure class="project-media">
      <img
        src="/assets/img/projects/test_latent_visualization.gif"
        alt="VAE Latent Spaces"
      />
    </figure>

    <div class="project-body">
      <p class="project-desc">
        Comparing reconstructions across latent sizes to illustrate the compression–fidelity trade-off.
      </p>
    </div>

    <aside class="project-meta">
      <div class="repo-embed">

        <a class="repo-embed__cardlink"
           href="https://github.com/MahanVeisi8/VAE-MNIST-Variable-Latent-Size-Reconstruction-and-Visualization">
          <div class="repo-embed__cardimg">
            <img
              src="https://github-readme-stats.vercel.app/api/pin/?username=MahanVeisi8&repo=VAE-MNIST-Variable-Latent-Size-Reconstruction-and-Visualization&theme=transparent&show_owner=true"
              alt="VAE MNIST repo card"
              loading="lazy"
            />
          </div>
        </a>

        <a class="repo-embed__btn"
           href="https://github.com/MahanVeisi8/VAE-MNIST-Variable-Latent-Size-Reconstruction-and-Visualization">
          <i class="fab fa-github"></i>
          View Repo
        </a>

      </div>
    </aside>

  </article>


  <!-- Denoising Emotion Dataset -->
  <article class="project-card project-card--triple">

    <header class="project-card__titlebar">
      <h3 class="project-title">Denoising Facial Emotion Dataset with Attention U-Net and GAN</h3>
    </header>

    <figure class="project-media">
      <img
        src="/assets/img/projects/denoising-emotion.png"
        alt="Denoising Emotion Dataset"
      />
    </figure>

    <div class="project-body">
      <p class="project-desc">
        Gaussian &amp; salt-and-pepper noise removal via Attention U-Net + PatchGAN, achieving strong PSNR/SSIM.
      </p>
    </div>

    <aside class="project-meta">
      <div class="repo-embed">

        <a class="repo-embed__cardlink"
           href="https://github.com/MahanVeisi8/From-Chaos-to-Clarity-Denoising-Images-with-UNet-and-GANs">
          <div class="repo-embed__cardimg">
            <img
              src="https://github-readme-stats.vercel.app/api/pin/?username=MahanVeisi8&repo=From-Chaos-to-Clarity-Denoising-Images-with-UNet-and-GANs&theme=transparent&show_owner=true"
              alt="Denoising repo card"
              loading="lazy"
            />
          </div>
        </a>

        <a class="repo-embed__btn"
           href="https://github.com/MahanVeisi8/From-Chaos-to-Clarity-Denoising-Images-with-UNet-and-GANs">
          <i class="fab fa-github"></i>
          View Repo
        </a>

      </div>
    </aside>

  </article>


  <!-- RL Practices -->
  <article class="project-card project-card--triple">

    <header class="project-card__titlebar">
      <h3 class="project-title">Reinforcement Learning Practices</h3>
    </header>

    <figure class="project-media">
      <img
        src="/assets/img/projects/rl-practices.gif"
        alt="Reinforcement Learning Practices"
      />
    </figure>

    <div class="project-body">
      <p class="project-desc">
        Hands-on study of classic RL algorithms with Boltzmann exploration tweaks.
      </p>
      <ul class="project-list">
        <li>DQN, SARSA, D3QN, and more</li>
      </ul>
    </div>

    <aside class="project-meta">
      <div class="repo-embed">

        <a class="repo-embed__cardlink"
           href="https://github.com/MahanVeisi8/RL_practices">
          <div class="repo-embed__cardimg">
            <img
              src="https://github-readme-stats.vercel.app/api/pin/?username=MahanVeisi8&repo=RL_practices&theme=transparent&show_owner=true"
              alt="RL Practices repo card"
              loading="lazy"
            />
          </div>
        </a>

        <a class="repo-embed__btn"
           href="https://github.com/MahanVeisi8/RL_practices">
          <i class="fab fa-github"></i>
          View Repo
        </a>

      </div>
    </aside>

  </article>


  <!-- Fashion Tagger -->
  <article class="project-card project-card--triple">

    <header class="project-card__titlebar">
      <h3 class="project-title">Fashion Tagger: AI-Powered Fashion Image Labeling</h3>
    </header>

    <figure class="project-media">
      <img
        src="/assets/img/projects/fashion-tagger.png"
        alt="Fashion Tagger: AI-Powered Fashion Image Labeling"
      />
    </figure>

    <div class="project-body">
      <p class="project-desc">
        Multi-label classifier trained on 44k images for real-time tagging and dataset organization.
      </p>
    </div>

    <aside class="project-meta">
      <div class="repo-embed">

        <a class="repo-embed__cardlink"
           href="https://github.com/MahanVeisi8/FashionTagger">
          <div class="repo-embed__cardimg">
            <img
              src="https://github-readme-stats.vercel.app/api/pin/?username=MahanVeisi8&repo=FashionTagger&theme=transparent&show_owner=true"
              alt="FashionTagger repo card"
              loading="lazy"
            />
          </div>
        </a>

        <a class="repo-embed__btn"
           href="https://github.com/MahanVeisi8/FashionTagger">
          <i class="fab fa-github"></i>
          View Repo
        </a>

      </div>
    </aside>

  </article>


  <!-- Face Recognition -->
  <article class="project-card project-card--triple">

    <header class="project-card__titlebar">
      <h3 class="project-title">Iranian Celebrity Face Recognition</h3>
    </header>

    <figure class="project-media">
      <img
        src="/assets/img/projects/face-recognition.gif"
        alt="Iranian Celebrity Face Recognition"
      />
    </figure>

    <div class="project-body">
      <p class="project-desc">
        CNN-based app (Flask + JS) for accurate real-time recognition of Iranian celebrities.
      </p>
    </div>

    <aside class="project-meta">
      <div class="repo-embed">

        <a class="repo-embed__cardlink"
           href="https://github.com/MahanVeisi8/Face_recognition">
          <div class="repo-embed__cardimg">
            <img
              src="https://github-readme-stats.vercel.app/api/pin/?username=MahanVeisi8&repo=Face_recognition&theme=transparent&show_owner=true"
              alt="Face Recognition repo card"
              loading="lazy"
            />
          </div>
        </a>

        <a class="repo-embed__btn"
           href="https://github.com/MahanVeisi8/Face_recognition">
          <i class="fab fa-github"></i>
          View Repo
        </a>

      </div>
    </aside>

  </article>


  <!-- Automated README Generator -->
  <article class="project-card project-card--triple">

    <header class="project-card__titlebar">
      <h3 class="project-title">Automated README Generator with Multi-Agent CrewAI</h3>
    </header>

    <figure class="project-media">
      <img
        src="/assets/img/projects/automated-readme-generator.jpg"
        alt="Automated README Generator with Multi-Agent CrewAI"
      />
    </figure>

    <div class="project-body">
      <p class="project-desc">
        LLaMA-3 + CrewAI pipeline for consistent, automated repository documentation.
      </p>
    </div>

    <aside class="project-meta">
      <div class="repo-embed">

        <a class="repo-embed__cardlink"
           href="https://github.com/MahanVeisi8/Automated-readme-generator-with-Multi-Agent-CrewAI">
          <div class="repo-embed__cardimg">
            <img
              src="https://github-readme-stats.vercel.app/api/pin/?username=MahanVeisi8&repo=Automated-readme-generator-with-Multi-Agent-CrewAI&theme=transparent&show_owner=true"
              alt="README Generator repo card"
              loading="lazy"
            />
          </div>
        </a>

        <a class="repo-embed__btn"
           href="https://github.com/MahanVeisi8/Automated-readme-generator-with-Multi-Agent-CrewAI">
          <i class="fab fa-github"></i>
          View Repo
        </a>

      </div>
    </aside>

  </article>


  <!-- Machine Learning Practices -->
  <article class="project-card project-card--triple">

    <header class="project-card__titlebar">
      <h3 class="project-title">Machine Learning Practices</h3>
    </header>

    <figure class="project-media">
      <img
        src="/assets/img/projects/ml-practices.png"
        alt="Machine Learning Practices"
      />
    </figure>

    <div class="project-body">
      <p class="project-desc">
        Hands-on survey of supervised learning techniques on diverse datasets.
      </p>
      <ul class="project-list">
        <li>KNN, SVC, Decision Trees, etc.</li>
      </ul>
    </div>

    <aside class="project-meta">
      <div class="repo-embed">

        <a class="repo-embed__cardlink"
           href="https://github.com/MahanVeisi8/MLPractices">
          <div class="repo-embed__cardimg">
            <img
              src="https://github-readme-stats.vercel.app/api/pin/?username=MahanVeisi8&repo=MLPractices&theme=transparent&show_owner=true"
              alt="MLPractices repo card"
              loading="lazy"
            />
          </div>
        </a>

        <a class="repo-embed__btn"
           href="https://github.com/MahanVeisi8/MLPractices">
          <i class="fab fa-github"></i>
          View Repo
        </a>

      </div>
    </aside>

  </article>

</section>
