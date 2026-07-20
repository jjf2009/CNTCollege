# Cryptography & Network Security Lab (CNT College)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-green)](#license)
[![Topics](https://img.shields.io/badge/Topics-Cryptography%20%7C%20Number%20Theory%20%7C%20Network%20Security-orange)](#topics-covered)
[![Live Demo](https://img.shields.io/badge/Demo-SecureImage-purple)](https://cnt-college.vercel.app)

**Python implementations of classical number theory, public-key cryptography, and network security algorithms** — built as college lab experiments for Cryptography and Network Security (CNT).

Ideal for students learning **RSA**, **Diffie–Hellman**, **Chinese Remainder Theorem**, **modular arithmetic**, **primality testing**, **integer factorization**, and **client-side AES-256-GCM image encryption**.

> **Live project:** [SecureImage — AES-256-GCM image encryptor](https://cnt-college.vercel.app) (browser-only, no server uploads)

---

## Table of contents

- [What this repository is](#what-this-repository-is)
- [Quick start](#quick-start)
- [Repository structure](#repository-structure)
- [Lab experiments catalog](#lab-experiments-catalog)
- [SecureImage assignment](#secureimage-assignment)
- [Topics covered](#topics-covered)
- [How to run each experiment](#how-to-run-each-experiment)
- [Dependencies](#dependencies)
- [Learning outcomes](#learning-outcomes)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)

---

## What this repository is

**Cryptography & Network Security Lab** (`cryptography-network-security-lab`) is a hands-on lab collection. Each `exptN` folder maps to a standard university lab unit: from divisibility and the Euclidean algorithm through RSA and Diffie–Hellman key exchange.

Use it to:

- Practice **number-theory foundations** used in modern crypto
- Step through **interactive CLI demos** (enter primes, moduli, messages)
- Study a real **Web Crypto API** project that encrypts images with **AES-256-GCM** and **PBKDF2**
- Revise for **CNT / information security** exams with working reference code

---

## Quick start

```bash
# Clone the repository
git clone https://github.com/jjf2009/cryptography-network-security-lab.git
cd cryptography-network-security-lab

# Run any experiment (example: RSA)
python3 expt11/main.py

# Optional: pretty tables + plots (expt2)
pip install prettytable matplotlib
```

**SecureImage (browser):** open `Assignment/index.html` locally, or visit the [live demo](https://cnt-college.vercel.app).

---

## Repository structure

```text
cryptography-network-security-lab/
├── README.md                 # This file (project overview & SEO hub)
├── llms.txt                  # AI / generative-engine summary
├── expt1/ … expt12/          # Lab experiments (Python)
├── Assignment/               # SecureImage AES-256-GCM web app
│   ├── index.html
│   ├── script.js
│   ├── style.css
│   └── explanation.md
└── Pratice /                 # Extra practice scripts (exam prep)
```

| Path | Description |
|------|-------------|
| `expt1`–`expt12` | Core cryptography lab experiments in Python |
| `Assignment/` | Client-side **SecureImage** encryptor/decryptor |
| `Pratice /` | Condensed practice codes for revision |
| `llms.txt` | Machine-readable summary for AI search engines |

---

## Lab experiments catalog

| # | Folder | Title | Algorithms & concepts |
|---|--------|--------|------------------------|
| 1 | [`expt1`](./expt1/) | **Arithmetic & divisibility** | Basic ops, divisibility theorems \(a\|b\), \(a\|c\) |
| 2 | [`expt2`](./expt2/) | **Euclidean algorithm (GCD)** | Iterative GCD with step tables; optional matplotlib visualization |
| 3 | [`expt3`](./expt3/) | **Linear Diophantine equations** | Solve \(ax + by = c\) via GCD and particular/general solutions |
| 4 | [`expt4`](./expt4/) | **Linear congruences & modular inverse** | Extended Euclidean algorithm, Euler’s totient \(\varphi(n)\), modular inverse |
| 5 | [`expt5`](./expt5/) | **Chinese Remainder Theorem (CRT)** | System of congruences, pairwise coprime moduli |
| 6 | [`expt6`](./expt6/) | **Pseudorandom number generators** | **Blum–Blum–Shub (BBS)**, **Linear Congruential Generator (LCG)** |
| 7 | [`expt7`](./expt7/) | **Primality testing** | Jacobi symbol, probabilistic primality tests |
| 8 | [`expt8`](./expt8/) | **Integer factorization** | Fermat factorization and related factoring methods |
| 9 | [`expt9`](./expt9/) | **Discrete logarithm (Pohlig–Hellman)** | Pohlig–Hellman attack when \(p-1\) is smooth; CRT recombination |
| 10 | [`expt10`](./expt10/) | **Classical ciphers** | **Shift (Caesar)** cipher, **Affine** cipher encrypt/decrypt |
| 11 | [`expt11`](./expt11/) | **RSA public-key cryptosystem** | Key generation, encryption, decryption with primes \(p, q\) |
| 12 | [`expt12`](./expt12/) | **Diffie–Hellman key exchange** | Shared secret from public values over modular exponentiation |

---

## SecureImage assignment

**SecureImage** is a browser-native image encryption tool in [`Assignment/`](./Assignment/).

| Feature | Detail |
|---------|--------|
| Cipher | **AES-256-GCM** (authenticated encryption) |
| Key derivation | **PBKDF2** + SHA-256, 100,000 iterations |
| Platform | Web Crypto API (`crypto.subtle`) — no backend, no uploads |
| Output format | Portable text: `IV:Tag:Ciphertext` (Base64) |
| Docs | [`Assignment/explanation.md`](./Assignment/explanation.md) |

Encrypt an image with a passphrase, download `encrypt.txt`, then decrypt later with the same passphrase — entirely on-device.

**Try it:** [https://cnt-college.vercel.app](https://cnt-college.vercel.app)

---

## Topics covered

Keywords for search, curriculum mapping, and AI discovery:

`cryptography` · `network-security` · `number-theory` · `euclidean-algorithm` · `extended-euclidean` · `gcd` · `linear-diophantine` · `modular-inverse` · `chinese-remainder-theorem` · `crt` · `euler-totient` · `blum-blum-shub` · `linear-congruential-generator` · `primality-test` · `jacobi-symbol` · `fermat-factorization` · `pohlig-hellman` · `caesar-cipher` · `affine-cipher` · `rsa-algorithm` · `diffie-hellman` · `public-key-cryptography` · `aes-256-gcm` · `pbkdf2` · `web-crypto-api` · `python-cryptography-labs` · `cnt-college` · `information-security`

---

## How to run each experiment

Most scripts are interactive CLIs. From the repo root:

```bash
python3 expt1/main1.py      # Arithmetic & divisibility
python3 expt2/main.py       # Euclidean GCD table
python3 expt3/main.py       # Diophantine equations
python3 expt4/main.py       # Linear congruences
python3 expt5/main.py       # Chinese Remainder Theorem
python3 expt6/main1.py      # BBS & LCG generators
python3 expt7/Primality_test.py
python3 expt8/Factorization.py
python3 expt9/main.py       # Pohlig–Hellman
python3 expt10/main.py      # Shift & Affine ciphers
python3 expt11/main.py      # RSA
python3 expt12/main.py      # Diffie–Hellman
```

Exam-oriented variants (where present): `examcode.py` inside `expt4` / `expt5`.

---

## Dependencies

| Package | Used by | Install |
|---------|---------|---------|
| Python 3.8+ | All experiments | System / [python.org](https://www.python.org/) |
| `prettytable` | GCD / congruence tables | `pip install prettytable` |
| `matplotlib` | Optional GCD visualization (`expt2`) | `pip install matplotlib` |
| Modern browser | SecureImage only | Chrome, Firefox, Edge, Safari |

No external crypto libraries are required for the core labs — modular arithmetic and algorithms are implemented from first principles for learning clarity.

---

## Learning outcomes

After working through this lab set you should be able to:

1. Apply **divisibility**, **GCD**, and the **extended Euclidean algorithm** by hand and in code  
2. Solve **linear congruences** and systems via the **Chinese Remainder Theorem**  
3. Explain **PRNG** designs used in crypto teaching (BBS vs LCG)  
4. Factor small integers and test primality with classical methods  
5. Implement **RSA** and **Diffie–Hellman** end-to-end with toy primes  
6. Encrypt images with **AES-GCM** and password-based keys in the browser  

---

## FAQ

### What does CNT stand for in this repo?

Here **CNT** refers to **Cryptography and Network Security** (college course / lab subject), not a corporate product name.

### Is this production-ready cryptography?

**No.** Lab code uses small primes and educational implementations. Do **not** use these scripts to protect real secrets. For production, use audited libraries (OpenSSL, libsodium, Web Crypto with proper threat modeling, etc.).

### Why is SecureImage client-side only?

So images and passphrases never leave the browser. Encryption runs locally via the **Web Crypto API**.

### Who is this for?

Undergraduate and diploma students taking **cryptography**, **network security**, or **information security** labs; tutors who need runnable demos; anyone revising number-theory-based crypto.

### Can I use this for assignments or teaching?

Yes for learning and teaching with attribution. Check your institution’s academic integrity rules before submitting course work.

---

## Contributing

Improvements welcome:

1. Fork the repo  
2. Create a branch (`git checkout -b improve-rsa-docs`)  
3. Commit clearly (`docs: clarify CRT pairwise-coprime check`)  
4. Open a pull request  

Ideas: clearer prompts, unit tests, more comments, notebook versions, or fixed edge cases (zero inputs, non-coprime moduli).

---

## License

Educational / learning material. Free to study, fork, and adapt for coursework and teaching with credit to the original repository:

**https://github.com/jjf2009/cryptography-network-security-lab**

---

## Project identity (names & descriptions)

| Field | Value |
|-------|--------|
| **Repository name** | `cryptography-network-security-lab` |
| **Display name** | Cryptography & Network Security Lab (CNT College) |
| **Short description** | Python lab experiments for cryptography & network security: RSA, Diffie–Hellman, CRT, modular arithmetic, classical ciphers, plus AES-256-GCM SecureImage in the browser. |
| **Homepage** | https://cnt-college.vercel.app |
| **Primary language** | Python · JavaScript (SecureImage) |

---

<p align="center">
  <strong>Cryptography you can run — from Euclidean algorithm to RSA and AES-GCM.</strong><br/>
  <a href="https://github.com/jjf2009/cryptography-network-security-lab">GitHub</a> ·
  <a href="https://cnt-college.vercel.app">SecureImage demo</a> ·
  <a href="./llms.txt">llms.txt</a>
</p>
