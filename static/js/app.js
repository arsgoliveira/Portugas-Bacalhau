/* ═══════════════════════════════════════════════════════════════
   Portugas Bacalhau — JavaScript Principal
   Partículas ✦ Animações ✦ Contadores ✦ Formulário
═══════════════════════════════════════════════════════════════ */

// ── Partículas Douradas ─────────────────────────────────────────
window.addEventListener('load', () => {
  if (typeof particlesJS === 'undefined') return;

    particlesJS('particles-js', {
    particles: {
      number: { value: 55, density: { enable: true, value_area: 900 } },
      color: { value: ['#D4AF37', '#FFD700', '#1E5799', '#003087', '#87CEEB', '#ffffff'] },
      shape: { type: 'circle' },
      opacity: { value: 0.35, random: true, anim: { enable: true, speed: 0.6, opacity_min: 0.1, sync: false } },
      size:    { value: 3.5, random: true, anim: { enable: true, speed: 2, size_min: 0.5, sync: false } },
      line_linked: { enable: true, distance: 130, color: '#FFD700', opacity: 0.08, width: 1 },
      move: {
        enable: true, speed: 1.8, direction: 'none', random: true,
        straight: false, out_mode: 'out', bounce: false
      }
    },
    interactivity: {
      detect_on: 'canvas',
      events: {
        onhover: { enable: true, mode: 'bubble' },
        onclick: { enable: true, mode: 'push' },
        resize: true
      },
      modes: {
        bubble: { distance: 180, size: 6, duration: 0.4, opacity: 0.7, speed: 3 },
        push:   { particles_nb: 3 }
      }
    },
    retina_detect: true
  });
});

// ── Loading Screen ──────────────────────────────────────────────
window.addEventListener('load', () => {
  const overlay = document.getElementById('loading');
  if (!overlay) return;
  setTimeout(() => overlay.classList.add('hidden'), 900);
});

// ── Navbar — scroll effect ──────────────────────────────────────
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar?.classList.toggle('scrolled', window.scrollY > 60);
}, { passive: true });

// ── Navbar — mobile toggle ──────────────────────────────────────
const navToggle = document.getElementById('navToggle');
const navLinks  = document.getElementById('navLinks');
navToggle?.addEventListener('click', () => {
  navLinks?.classList.toggle('open');
});
document.addEventListener('click', (e) => {
  if (!navbar?.contains(e.target)) navLinks?.classList.remove('open');
});

// ── Scroll Animations (IntersectionObserver) ────────────────────
const animObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      animObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.animate-on-scroll').forEach(el => animObserver.observe(el));

// ── Contadores Animados ─────────────────────────────────────────
function animateCounter(el, target, duration = 2200) {
  const startTime = performance.now();

  function tick(now) {
    const progress = Math.min((now - startTime) / duration, 1);
    // easing: ease-out cubic
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = Math.round(eased * target);
    el.textContent = current.toLocaleString('pt-PT') + '+';
    if (progress < 1) requestAnimationFrame(tick);
    else el.textContent = target.toLocaleString('pt-PT') + (target > 4 ? '+' : '');
  }
  requestAnimationFrame(tick);
}

const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting && !entry.target.dataset.done) {
      entry.target.dataset.done = 'true';
      animateCounter(entry.target, parseInt(entry.target.dataset.counter));
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('[data-counter]').forEach(el => counterObserver.observe(el));

// ── Filtros de Produtos ─────────────────────────────────────────
const filtroButtons = document.querySelectorAll('.filtro-btn');
const wrappers      = document.querySelectorAll('.produto-card-wrapper');

filtroButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    filtroButtons.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    const cat = btn.dataset.categoria;
    wrappers.forEach((card, i) => {
      const show = cat === 'todos' || card.dataset.categoria === cat;
      card.style.transition = `opacity 0.35s ease ${i * 0.04}s, transform 0.35s ease ${i * 0.04}s`;
      if (show) {
        card.style.display = 'block';
        requestAnimationFrame(() => {
          card.style.opacity = '1';
          card.style.transform = 'translateY(0)';
        });
      } else {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        setTimeout(() => { card.style.display = 'none'; }, 350);
      }
    });
  });
});

// ── Formulário de Contacto ──────────────────────────────────────
const contactForm = document.getElementById('contactForm');
contactForm?.addEventListener('submit', async (e) => {
  e.preventDefault();

  const btn = contactForm.querySelector('.btn-submit');
  const originalText = btn.innerHTML;
  btn.disabled = true;
  btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> A enviar…';

  const body = {
    nome:      contactForm.querySelector('[name="nome"]')?.value,
    email:     contactForm.querySelector('[name="email"]')?.value,
    mensagem:  contactForm.querySelector('[name="mensagem"]')?.value,
    telefone:  contactForm.querySelector('[name="telefone"]')?.value || null
  };

  try {
    const res    = await fetch('/api/contacto', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    });
    const result = await res.json();

    if (result.sucesso) {
      showToast('✅ ' + result.mensagem, 'success');
      contactForm.reset();
    } else {
      throw new Error('Erro no servidor');
    }
  } catch {
    showToast('❌ Não foi possível enviar. Tente novamente.', 'error');
  }

  btn.disabled = false;
  btn.innerHTML = originalText;
});

// ── Toast ───────────────────────────────────────────────────────
function showToast(message, type = 'success') {
  const toast = document.getElementById('toast');
  if (!toast) return;
  toast.textContent = message;
  toast.className = 'toast show' + (type === 'error' ? ' error' : '');
  clearTimeout(toast._timer);
  toast._timer = setTimeout(() => toast.classList.remove('show'), 4500);
}

// ── Flip Cards — toque em mobile ────────────────────────────────
document.querySelectorAll('.flip-card').forEach(card => {
  card.addEventListener('click', () => card.classList.toggle('flipped'));
});

// ── Smooth scroll para âncoras ──────────────────────────────────
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', (e) => {
    const target = document.querySelector(a.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});

// ── Efeito de brilho nos botões ─────────────────────────────────
document.querySelectorAll('.btn').forEach(btn => {
  btn.addEventListener('mousemove', (e) => {
    const rect = btn.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width  * 100).toFixed(0);
    const y = ((e.clientY - rect.top)  / rect.height * 100).toFixed(0);
    btn.style.setProperty('--mx', `${x}%`);
    btn.style.setProperty('--my', `${y}%`);
  });
});
