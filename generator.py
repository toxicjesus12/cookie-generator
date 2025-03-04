import random
from datetime import datetime, timedelta
from rich.prompt import Confirm, IntPrompt, Prompt
from rich.console import Console
from faker import Faker
from presets import DEVICE_PRESETS, USER_AGENT_PRESETS

console = Console()
fake = Faker()

class CookieGenerator:
    def __init__(self):
        self.devices = DEVICE_PRESETS
        self.user_agents = USER_AGENT_PRESETS
    
    def generate_fingerprint(self, device_type):
        return {
            'user_agent': self._get_user_agent(device_type),
            'screen_res': random.choice(self.devices[device_type]['resolutions']),
            'timezone': fake.timezone(),
            'fonts': self._get_font_stack(device_type),
            'platform': random.choice(self.devices[device_type]['platforms']),
            'device_model': random.choice(self.devices[device_type]['models'])
        }
    
    def _get_user_agent(self, device_type):
        return random.choice(self.user_agents[device_type])

class CookieProfile:
    def __init__(self):
        self.gen = CookieGenerator()
        self.profile = {}
    
    def configure(self):
        self._select_device()
        self._set_geolocation()
        self._configure_network()
        self._generate_cookies()
    
    def _select_device(self):
        device = Prompt.ask(
            "[cyan]Device type[/]",
            choices=["mobile", "desktop", "tablet"],
            default="desktop"
        )
        self.profile.update(self.gen.generate_fingerprint(device))
    
    def _configure_network(self):
        if Confirm.ask("[cyan]Use SOCKS5 proxy?[/]"):
            self._setup_proxy()
    
    def _setup_proxy(self):
        proxy = Prompt.ask(
            "[yellow]Proxy (host:port:user:pass)[/]",
            default="proxy.example.com:1080:user123:pass456"
        )
        host, port, user, pwd = proxy.split(':')
        self.profile['proxy'] = f"socks5://{user}:{pwd}@{host}:{port}"
    
    def _generate_cookies(self):
        cookies = []
        base_expiry = datetime.now() + timedelta(days=random.randint(90, 180))
        
        for _ in range(random.randint(8, 15)):
            cookies.append({
                "name": f"{fake.word()}_session",
                "value": fake.sha256(),
                "expires": base_expiry.strftime("%a, %d %b %Y %H:%M:%S GMT"),
                "http_only": random.choice([True, False]),
                "secure": random.choice([True, False])
            })
        self.profile['cookies'] = cookies
