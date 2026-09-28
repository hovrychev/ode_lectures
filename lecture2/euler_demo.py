"""Числа для слайдов 28, 31–32 и упражнения 7. Только стандартная библиотека.

Запуск: python3 lecture2/euler_demo.py
Все расчёты выполняются в обычной арифметике float.
"""

from math import exp


def euler(f, t0, x0, step, count):
    """Вернуть узлы и значения явного метода Эйлера."""
    values = [(t0, x0)]
    x = x0
    for n in range(count):
        t = t0 + n * step
        x += step * f(t, x)
        values.append((t0 + (n + 1) * step, x))
    return values


def main():
    exact = exp(-1)
    print("Слайд 28: x'=-x, x(0)=1, T=1")
    print("h        N       X_N       абсолютная ошибка")
    for count in (5, 10, 20, 40):
        step = 1 / count
        approx = euler(lambda t, x: -x, 0, 1, step, count)[-1][1]
        print(f"{step:<8g} {count:<4d} {approx:.6f}  {abs(approx-exact):.6f}")
    print("\nСлайд 32: значения для двух ломаных")
    for step, count in ((1.5, 5), (2.2, 3)):
        print(f"h={step}: {euler(lambda t, x: -x, 0, 1, step, count)}")
    approx = euler(lambda t, x: -2*x, 0, 1, 0.25, 2)[-1][1]
    print(f"\nУпражнение 7: X_2={approx}, точное={exact:.6f}, ошибка={abs(approx-exact):.6f}")


if __name__ == "__main__":
    main()
