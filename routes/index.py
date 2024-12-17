from flask import Blueprint, redirect, render_template, session
from utils import login_required

bp = Blueprint("index", __name__)


@bp.route("/")
@login_required
def index():
    return redirect(
        "/survey"
        if session.get("role") == "alumnus"
        else (
            "/stats"
            if "stats" in session.get("perms")
            else (
                "/manage"
                if "manage" in session.get("perms")
                else (
                    "/announce"
                    if "announce" in session.get("perms")
                    else "/mod" if "mod" in session.get("perms") else "/news"
                )
            )
        )
    )


@bp.route("/about")
def about():
    about = {
        "What is Alumni System": "The Alumni System at Al-Balqa Applied University is a vital tool for strengthening the relationship between the university and its graduates, contributing to the growth of both the institution and the personal and professional development of its alumni.",
        "What Alumni Can Do": "Through this system, the university can track and update alumni's personal and professional information, organize career-related events and services, and facilitate connections among graduates and university staff. This enhances alumni networks and provides continuous opportunities for career advancement and professional development.",
        "Alumni and Graduates": "The system empowers graduates by enabling them to expand their professional networks, exchange knowledge, and collaborate with peers on projects or career guidance. It serves as a platform for fostering both personal and professional growth while bridging the gap between academia and the workforce.",
        "Career Opportunities": "Facilitating access to job opportunities, mentorship, and career-related resources, the system ensures that graduates remain connected to their alma mater and benefit from lifelong learning.",
        "Strategic Partnerships": "The Alumni System strengthens the university's ability to form strategic partnerships with local and international organizations, creating pathways for internships, research opportunities, and joint initiatives. These partnerships not only contribute to the community's economy but also elevate the university's reputation in academic, professional, and industrial domains.",
        "Alumni Engagement": "The system acts as a hub for alumni engagement by hosting events, sharing updates, and fostering a sense of belonging. It enables graduates to actively participate in university activities, contribute to decision-making processes, and advocate for future developments.",
    }
    return render_template("about.jinja", about=about)
