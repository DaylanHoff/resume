#!/usr/bin/env python3
"""Generate Daylan Hoff one-page resume PDF (Cloud Engineer tailored)."""

from pathlib import Path

from fpdf import FPDF

OUT = Path(__file__).resolve().parent / "Daylan_Hoff_Resume.pdf"
PAGE_W, PAGE_H = 215.9, 279.4
ML, MR, MT, MB = 12.5, 12.5, 10, 10
CW = PAGE_W - ML - MR


class Resume(FPDF):
    def __init__(self):
        super().__init__(format="Letter", unit="mm")
        self.set_auto_page_break(auto=True, margin=MB)
        self.set_margins(ML, MT, MR)
        self.add_page()

    def rule(self, heavy=False):
        y = self.get_y()
        self.set_draw_color(35, 55, 90) if heavy else self.set_draw_color(170, 180, 195)
        self.set_line_width(0.5 if heavy else 0.22)
        self.line(ML, y, PAGE_W - MR, y)
        self.ln(2.2 if heavy else 1.8)

    def section(self, title):
        self.ln(0.6)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(25, 45, 80)
        self.cell(CW, 4.8, title.upper(), new_x="LMARGIN", new_y="NEXT")
        self.rule(False)

    def bullets(self, items, lh=3.55):
        self.set_font("Helvetica", "", 8.3)
        self.set_text_color(28, 33, 42)
        for item in items:
            self.set_x(ML)
            self.cell(3.2, lh, "-")
            self.multi_cell(CW - 3.2, lh, item)
            self.ln(0.15)
        self.ln(0.7)

    def job(self, left, right):
        self.set_font("Helvetica", "B", 9.2)
        self.set_text_color(20, 30, 48)
        self.cell(CW * 0.58, 4.2, left)
        self.set_font("Helvetica", "", 7.8)
        self.set_text_color(70, 80, 95)
        self.cell(CW * 0.42, 4.2, right, align="R", new_x="LMARGIN", new_y="NEXT")

    def sub(self, text):
        self.set_font("Helvetica", "I", 7.8)
        self.set_text_color(70, 80, 95)
        self.multi_cell(CW, 3.4, text)
        self.ln(0.2)

    def skill(self, label, body):
        self.set_font("Helvetica", "B", 8.1)
        self.set_text_color(25, 40, 70)
        lw = self.get_string_width(label) + 1.2
        self.cell(lw, 3.55, label)
        self.set_font("Helvetica", "", 8.1)
        self.set_text_color(28, 33, 42)
        self.multi_cell(CW - lw, 3.55, body)
        self.ln(0.15)


def build():
    pdf = Resume()

    pdf.set_y(MT)
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(20, 30, 48)
    pdf.cell(CW, 6.5, "Daylan Hoff", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 8.5)
    pdf.set_text_color(55, 65, 80)
    pdf.cell(
        CW,
        4.2,
        "daylan.hoff@gmail.com  |  St. George, Utah  |  435-592-5991",
        align="C",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.ln(1.2)
    pdf.rule(True)

    pdf.section("Professional Summary")
    pdf.set_font("Helvetica", "", 8.3)
    pdf.set_text_color(28, 33, 42)
    pdf.multi_cell(
        CW,
        3.55,
        "Cloud and platform engineer with 4+ years building, securing, and operating production "
        "infrastructure. Hands-on with Kubernetes, AWS, CI/CD, and containerized workloads at scale, "
        "including zero-downtime releases for 500+ applications. Delivers full-stack and DevOps "
        "solutions for mission-oriented organizations - from healthcare SaaS to tactical training "
        "platforms - with a focus on reliability, cost efficiency, and secure deployment.",
    )
    pdf.ln(0.8)

    pdf.section("Core Skills")
    pdf.skill(
        "Cloud & Platform:",
        " AWS (architecture, EC2 migration, cost optimization), Kubernetes, ArgoCD, containers, "
        "compute/networking/storage",
    )
    pdf.skill(
        "CI/CD & DevOps:",
        " Azure DevOps, Jenkins/CloudBees migrations, GitHub Actions, blue-green deployments, "
        "release automation, GitOps",
    )
    pdf.skill(
        "Security & Compliance:",
        " DevSecOps workflows, HIPAA-aligned production systems, JWT auth, encryption, "
        "least-privilege access",
    )
    pdf.skill(
        "Languages & Tooling:",
        " C#, Python, JavaScript/TypeScript, .NET, scripting, Cloudflare Workers/Pages, Wrangler",
    )
    pdf.skill(
        "Practices:",
        " Agile/Scrum leadership, cross-team release coordination, cost governance, operational reliability",
    )
    pdf.ln(0.5)

    pdf.section("Relevant Experience")

    pdf.job("Sr. DevOps Engineer, AdvancedMD", "Remote  |  05/2022 - Present")
    pdf.sub(
        "Cloud architecture, Kubernetes platform engineering, and CI/CD for large-scale healthcare SaaS"
    )
    pdf.bullets(
        [
            "Designed AWS cloud architecture supporting 500+ internal/external apps across compute, networking, and storage.",
            "Saved $600,000+ in 2023 cloud costs by migrating workloads off EC2 using AWS best practices and right-sized platform patterns.",
            "Automated CloudBees (Jenkins) to Azure DevOps migration with standardized release pipelines for 500+ applications.",
            "Built a Kubernetes + ArgoCD release framework that sustained zero downtime deployments for two consecutive years.",
            "Led release nights with blue-green strategies for 50+ apps; improved support resolution turnaround by 40%+ with leadership/dev/QA partners.",
            "Shipped critical platform components in .NET, C#, and JavaScript that eliminated three major production crash root causes.",
        ]
    )

    pdf.job(
        "Quality Assurance Engineer, AdvancedMD",
        "Hybrid, Salt Lake City, UT  |  06/2021 - 05/2022",
    )
    pdf.bullets(
        [
            "Automated API testing with Postman covering 90% of 500+ apps in 3 months; reduced pre-release defects by 40%.",
            "Cut release-night duration by ~3 hours via developer-QA workflow tooling (C#, Python); led Scrum across 4 engineering teams.",
            "One of two interns offered immediate full-time roles after strong systems and vulnerability analysis.",
        ]
    )

    pdf.job(
        "Full Stack & DevOps Engineer, Striker Training Complex (Contract)",
        "Texas / Remote  |  03/2026 - Present",
    )
    pdf.sub(
        "Web, recruiting, and platform infrastructure for a mission-focused tactical training organization"
    )
    pdf.bullets(
        [
            "Owned end-to-end public web and recruiting infrastructure for a tactical training company.",
            "Built multi-tenant CRM/ops platform (Next.js/TypeScript, Cloudflare Workers API, D1) with auth, RBAC, events, invoicing, and Stripe.",
            "Implemented secure API patterns (JWT refresh tokens, AES-256-GCM) and multi-environment CI/CD via GitHub Actions + Wrangler.",
            "Delivered Vite marketing/careers/training/store site integrated with the CRM API; managed edge compute, DNS, storage, and env isolation.",
        ]
    )

    pdf.job(
        "Web Platform Engineer, Providence Steward (Contract)",
        "Remote  |  04/2026 - 06/2026",
    )
    pdf.bullets(
        [
            "Delivered tax-firm production site (Next.js, TypeScript, Tailwind) with GitHub Actions CI/CD to Cloudflare Pages and low-ops edge hosting.",
        ]
    )

    pdf.section("Earlier Experience")
    pdf.set_font("Helvetica", "", 8.1)
    pdf.set_text_color(28, 33, 42)
    pdf.cell(CW * 0.72, 3.6, "Advanced Repair Specialist, Neumont College - Salt Lake City, UT")
    pdf.cell(CW * 0.28, 3.6, "2018 - 2021", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(CW * 0.72, 3.6, "Customer Service Agent, Phoenix Digital Group - Remote")
    pdf.cell(CW * 0.28, 3.6, "2015 - 2018", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(0.8)

    pdf.section("Certifications")
    pdf.set_font("Helvetica", "B", 8.1)
    pdf.set_text_color(20, 30, 48)
    pdf.cell(38, 3.6, "HIPAA Compliance")
    pdf.set_font("Helvetica", "", 8.1)
    pdf.set_text_color(28, 33, 42)
    pdf.multi_cell(
        CW - 38,
        3.6,
        "  09/2024 - 09/2025  |  Required for sensitive healthcare data and regulated production systems.",
    )
    pdf.ln(0.6)

    pdf.section("Education")
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_text_color(20, 30, 48)
    pdf.cell(CW * 0.62, 3.8, "Bachelor of Computer Science, Neumont College")
    pdf.set_font("Helvetica", "", 7.8)
    pdf.set_text_color(70, 80, 95)
    pdf.cell(CW * 0.38, 3.8, "Salt Lake City, UT  |  2018 - 2021", align="R")

    pdf.output(OUT)
    print(f"Wrote {OUT} ({pdf.page_no()} page)")


if __name__ == "__main__":
    build()
