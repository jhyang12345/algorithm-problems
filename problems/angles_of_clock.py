# Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.

def calcAngle(h, m):
    minutes = 60
    h_angle = h * 30 + (m / 2)
    m_angle = m * 6
    diff = max(m_angle, h_angle) - min(m_angle, h_angle)

    return min(diff, 360 - diff)

print(calcAngle(3, 30))

print(calcAngle(12, 30))
