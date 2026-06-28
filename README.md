https://orcid.org/my-orcid?orcid=0009-0004-1872-1153
https://doi.org/10.5281/zenodo.21009339
------------
# DroneWar GRA AI Officer

**Билингвальный (RU/EN) ИИ-офицер войны дронов на базе General Resonance Architecture (GRA).**
Без людей-дроноводов: вся логика управления разноплановыми БПЛА (РЛЕВ, РЭР, РЭБ, midstrike, deepstrike, ближний удар) работает через GRA-обнулёнку.

## English

Fully autonomous swarm command system. An AI officer composed of GRA-subjects orchestrates reconnaissance, electronic warfare, and multi-range strikes. The core principle is **GRA nullification** – any perturbation (noise, jamming, loss) is instantly annihilated into a zero vector while maintaining hierarchical stability.

- **Backend**: FastAPI + Python 3.10+
- **Frontend**: Vanilla JS dashboard with real-time resonance metrics
- **Theory**: GRA nullification, chiral resonance, love-oriented synchronization
- **Verification**: Monte Carlo combat simulations, unit tests

### Quick Start
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
Open `frontend/index.html` in browser.

---

## Русский

Полностью автономная система командования роем дронов. ИИ-офицер, составленный из GRA-субъектов, управляет разведкой, РЭБ и ударами на разную дальность. Основа – **GRA-обнулёнка**: любое возмущение (помеха, потеря связи) сводится к нулевому вектору, сохраняя иерархическую устойчивость.

### Быстрый старт
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
Откройте `frontend/index.html` в браузере.

## License
MIT (см. LICENSE)
