---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
published: true
classes: wide   # <-- makes the content area wider (Minimal Mistakes feature)
---

## Conference and Journal Papers

<section class="pub-grid">

  <!-- 1) MRI Reconstruction (two images) -->
  <article class="pub-card">
    <div class="pub-hero two">
      <img src="/assets/img/publications/CMRI_Recon.jpg" alt="MRI Reconstruction: k-space & pipeline">
      <img src="/assets/img/publications/CMRI_Recon_2.png" alt="MRI Reconstruction: qualitative comparison">
    </div>

    <div class="pub-body">
      <header class="pub-head">
        <h3 class="pub-title">All-in-One MRI Reconstruction with Cascaded Transformers</h3>
        <span class="pub-status">Manuscript In Progress</span>
      </header>

      <div class="pub-authors">
        <strong>Mahan Veisi</strong>
        <a href="https://scholar.google.com/citations?user=gHVVhW4AAAAJ&hl=en">
          <i class="ai ai-google-scholar ai-sm" aria-hidden="true"></i> Kian Anvari
        </a>
        <a href="https://scholar.google.com/citations?user=D_mPA6sAAAAJ&hl=en">
          <i class="ai ai-google-scholar ai-sm" aria-hidden="true"></i> Shahabedin Nabavi
        </a>
        <a href="https://scholar.google.com/citations?user=trWxrgcAAAAJ&hl=en">
          <i class="ai ai-google-scholar ai-sm" aria-hidden="true"></i> Mohsen Ebrahimi Moghaddam
        </a>
      </div>

      <div class="pub-actions">
        <!-- icons only; add hrefs as they go live -->
        <a class="icon-btn" title="arXiv/PDF" href="#" aria-label="arXiv"><i class="ai ai-arxiv" aria-hidden="true"></i></a>
        <a class="icon-btn" title="GitHub" href="#" aria-label="GitHub"><i class="fab fa-github" aria-hidden="true"></i></a>
      </div>

      <details class="pub-more">
        <summary>
          <span class="caret"></span>
          <span class="more">Show more</span><span class="less">Hide</span>
        </summary>
        <div class="pub-abstract">
          Cascaded transformer U-Nets with Frequency Mining for efficient multi-contrast MRI
          reconstruction from k-space; designed for MICCAI-style reconstruction benchmarks.
        </div>
      </details>
    </div>
  </article>

  <!-- 2) Airfoil (single image) -->
  <article class="pub-card">
    <div class="pub-hero one">
      <img src="/assets/img/publications/airfoil_diff_opt.jpg" alt="Diffusion-driven airfoil optimization">
    </div>

    <div class="pub-body">
      <header class="pub-head">
        <h3 class="pub-title">Diffusion-Driven Airfoil Optimization</h3>
      </header>

      <div class="pub-authors">
        <strong>Mahan Veisi</strong>
        <a href="https://scholar.google.de/citations?user=k2TvtoAAAAAJ">
          <i class="ai ai-google-scholar ai-sm" aria-hidden="true"></i> Navid Ansari
        </a>
        <a href="https://scholar.google.de/citations?user=Yjh-GHsAAAAJ">
          <i class="ai ai-google-scholar ai-sm" aria-hidden="true"></i> Vahid Babaei
        </a>
      </div>

      <div class="pub-actions">
        <a class="icon-btn" title="arXiv/PDF" href="#" aria-label="arXiv"><i class="ai ai-arxiv" aria-hidden="true"></i></a>
        <a class="icon-btn" title="GitHub" href="#" aria-label="GitHub"><i class="fab fa-github" aria-hidden="true"></i></a>
      </div>

      <details class="pub-more">
        <summary><span class="caret"></span><span class="more">Show more</span><span class="less">Hide</span></summary>
        <div class="pub-abstract">
          Latent-space diffusion + neural multi-objective Bayesian optimization for inverse designing
          2D airfoils, balancing lift–drag while promoting aerodynamic novelty.
        </div>
      </details>
    </div>
  </article>

  <!-- 3) DRL Stock Trading (two images) -->
  <article class="pub-card">
    <div class="pub-hero two">
      <img src="/assets/img/publications/deep-rl-stock-trading_1.png" alt="Equity curves across strategies">
      <img src="/assets/img/publications/deep-rl-stock-trading-arch.png" alt="PPO-LSTM + FinBERT architecture">
    </div>

    <div class="pub-body">
      <header class="pub-head">
        <h3 class="pub-title">Deep Reinforcement Learning for Stock Trading</h3>
        <span class="pub-status">IEEE ICCKE 2024</span>
      </header>

      <div class="pub-authors">
        <strong>Mahan Veisi</strong>, Sadra Berangi
        <a href="https://scholar.google.com/citations?user=QufpdNgAAAAJ&hl=en">
          <i class="ai ai-google-scholar ai-sm" aria-hidden="true"></i> Mahdi Shahbazi Khojasteh
        </a>
        <a href="https://scholar.google.com/citations?user=akmKmMQAAAAJ&hl=en">
          <i class="ai ai-google-scholar ai-sm" aria-hidden="true"></i> Armin Salimi-Badr
        </a>
      </div>

      <div class="pub-actions">
        <a class="icon-btn" title="IEEE Xplore" href="https://ieeexplore.ieee.org/document/10874515" aria-label="PDF"><i class="far fa-file-pdf" aria-hidden="true"></i></a>
        <a class="icon-btn" title="GitHub" href="https://github.com/MahanVeisi8/LSTMppo-DRL-StockTrader" aria-label="GitHub"><i class="fab fa-github" aria-hidden="true"></i></a>
        <a class="icon-btn" title="YouTube" href="https://youtu.be/Jfpc6_kGLYo?si=U9xVX03Jn_7jxY1d" aria-label="YouTube"><i class="fab fa-youtube" aria-hidden="true"></i></a>
      </div>

      <details class="pub-more">
        <summary><span class="caret"></span><span class="more">Show more</span><span class="less">Hide</span></summary>
        <div class="pub-abstract">
          FinBERT sentiment fused with PPO-LSTM. Reached <strong>134.39% cumulative return</strong> and
          <strong>1.46 Sharpe</strong>, outperforming DJIA, Ensemble, and PPO baselines.
        </div>
      </details>
    </div>
  </article>

  <!-- 4) SincNet PD (two images) -->
  <article class="pub-card">
    <div class="pub-hero two">
      <img src="/assets/img/publications/SincNet.jpg" alt="SincNet overview for gait classification">
      <img src="/assets/img/publications/SincNet_2.png" alt="Learned Sinc filters / salient frequency bands">
    </div>

    <div class="pub-body">
      <header class="pub-head">
        <h3 class="pub-title">SincNet for Parkinson’s Disease Detection</h3>
        <span class="pub-status">Under Review — AIHC Journal</span>
      </header>

      <div class="pub-authors">
        <a href="https://scholar.google.com/citations?user=akmKmMQAAAAJ&hl=en">
          <i class="ai ai-google-scholar ai-sm" aria-hidden="true"></i> Armin Salimi-Badr
        </a>,
        <strong>Mahan Veisi</strong>, Sadra Berangi
      </div>

      <div class="pub-actions">
        <a class="icon-btn" title="arXiv" href="https://www.arxiv.org/abs/2502.17463" aria-label="arXiv"><i class="ai ai-arxiv" aria-hidden="true"></i></a>
        <a class="icon-btn" title="GitHub" href="https://github.com/MahanVeisi8/Explainable-PD-Diagnosis-using-SincNet-and-Gait-Analysis" aria-label="GitHub"><i class="fab fa-github" aria-hidden="true"></i></a>
      </div>

      <details class="pub-more">
        <summary><span class="caret"></span><span class="more">Show more</span><span class="less">Hide</span></summary>
        <div class="pub-abstract">
          SincNet-based gait classification with post-hoc filter clustering to surface key frequency
          bands; achieved <strong>98.7% accuracy</strong> with explainable components.
        </div>
      </details>
    </div>
  </article>

  <!-- 5) RoboCup (single image) -->
  <article class="pub-card">
    <div class="pub-hero one">
      <img src="/assets/img/publications/Soccer2d.png" alt="RoboCup Soccer Simulation">
    </div>

    <div class="pub-body">
      <header class="pub-head">
        <h3 class="pub-title">Intelligent Agents for RoboCup Soccer Simulation</h3>
        <span class="pub-status">RoboCup Proceedings</span>
      </header>

      <div class="pub-authors">
        Mohammad Hesam Nasiri, Seyed Hassan Majid Zonouzi, Arya Parvizi, Seyed Mostafa Atyabi,
        Seyedeh Rana Rokni, Sanaz Moosapour, <strong>Mahan Veisi</strong>, Kiarah Kowsari, Farbod Saghfi
      </div>

      <div class="pub-actions">
        <a class="icon-btn" title="Paper (PDF)" href="https://archive.robocup.info/Soccer/Simulation/2D/TDPs/RoboCup/2023/R3CESBU_SS2D_RC2023_TDP.pdf" aria-label="PDF"><i class="far fa-file-pdf" aria-hidden="true"></i></a>
      </div>

      <details class="pub-more">
        <summary><span class="caret"></span><span class="more">Show more</span><span class="less">Hide</span></summary>
        <div class="pub-abstract">
          Role-optimized agents (goalkeeping, defense, teamwork) in the 2D Simulation League;
          team placed 2nd at IranOpen 2023.
        </div>
      </details>
    </div>
  </article>

</section>
