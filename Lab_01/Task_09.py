def max_bunch_count(source):
    m_streak=0
    o_streak = 0
    for i in range(len(source)):
        if i == len(source)-1:
            return (m_streak+1)
        elif source[i] == source[i+1]:
            o_streak += 1
        else:
            o_streak =0
        if o_streak >= m_streak:
            m_streak = o_streak

source= [1,1,2, 2, 1, 1,1,1]
print(max_bunch_count(source))