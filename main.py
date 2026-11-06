"""
AI User-Tester: Điểm khởi chạy kiểm thử trải nghiệm người dùng với AI.
"""
import os
import sys
import yaml
import asyncio
import argparse
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from dotenv import load_dotenv

from src.agent import UsabilityAgent
from src.reporter import generate_markdown_report, calculate_sus_score, get_sus_grade

load_dotenv()
console = Console()


def load_persona(persona_name: str) -> dict:
    """Đọc cấu hình Persona từ thư mục personas/"""
    persona_path = f"./personas/{persona_name}.yaml"
    if not os.path.exists(persona_path):
        console.print(f"[red]❌ Không tìm thấy file persona: {persona_path}[/red]")
        sys.exit(1)
        
    with open(persona_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


async def main():
    parser = argparse.ArgumentParser(description="AI Synthetic User Testing & Think-Aloud Usability Evaluator")
    parser.add_argument("--url", type=str, default="https://news.ycombinator.com", help="Địa chỉ web cần kiểm thử trải nghiệm")
    parser.add_argument("--persona", type=str, default="senior_user", choices=["senior_user", "busy_shopper", "tech_savvy"], help="Hồ sơ người dùng giả lập")
    parser.add_argument("--goal", type=str, default="Tìm kiếm bài viết thú vị và mở đọc nội dung", help="Mục tiêu người dùng muốn hoàn thành")
    parser.add_argument("--steps", type=int, default=4, help="Số bước thao tác tối đa")
    parser.add_argument("--headless", action="store_true", help="Chạy ẩn trình duyệt (không hiện cửa sổ)")
    args = parser.parse_args()

    console.print(Panel.fit(
        "[bold cyan]🤖 AI User-Tester: Synthetic Usability Engine[/bold cyan]\n"
        "[italic white]Mô phỏng người dùng thật bằng Vision AI & Think-Aloud Protocol[/italic white]",
        border_style="cyan"
    ))

    # 1. Load Persona
    persona = load_persona(args.persona)

    # 2. Hiển thị thông tin phiên test
    table = Table(title="Thông số phiên kiểm thử", border_style="dim")
    table.add_column("Thuộc tính", style="bold yellow")
    table.add_column("Giá trị", style="white")
    table.add_row("Hồ sơ (Persona)", f"{persona.get('name')} ({persona.get('age')} tuổi)")
    table.add_row("Trình độ công nghệ", str(persona.get("tech_literacy")))
    table.add_row("Trang web", args.url)
    table.add_row("Mục tiêu (Goal)", args.goal)
    table.add_row("Chế độ hiển thị", "Headless (Ẩn)" if args.headless else "Có cửa sổ trực quan")
    console.print(table)

    # 3. Chạy Agent
    agent = UsabilityAgent(
        persona=persona,
        goal=args.goal,
        start_url=args.url,
        max_steps=args.steps,
        headless=args.headless
    )
    
    session_data = await agent.run()

    # 4. Xuất Báo Cáo
    report_path = generate_markdown_report(session_data, output_dir="./reports")
    sus_score = calculate_sus_score(session_data.get("sus_answers", []))
    grade = get_sus_grade(sus_score)

    console.print("\n" + "="*60)
    console.print(f"[bold green]✅ Đã hoàn tất buổi kiểm thử trải nghiệm![/bold green]")
    console.print(f"📊 [bold]Điểm khả dụng (SUS Score):[/bold] [cyan]{sus_score}/100[/cyan] ({grade})")
    console.print(f"📄 [bold]Báo cáo chi tiết đã lưu tại:[/bold] [yellow]{report_path}[/yellow]")
    console.print("="*60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
