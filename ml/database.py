import sqlite3

conn = sqlite3.connect("injuries.db")
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS injuries (
               injury_name TEXT,
               description TEXT,
               training_plan TEXT
            )
               ''')

cursor.execute('''
ALTER TABLE injuries ADD COLUMN exercises TEXT;
''')

injuries_data = [
    # Injury: Hamstring Strain
    (
        'Hamstring Strain',
        'An injury to the muscles at the back of the thigh, often caused by rapid acceleration activities.',
        'Initial rest followed by gentle stretching; progressive strengthening exercises focusing on the hamstrings and gluteal muscles.',
        '3 sets of 15 reps of gentle hamstring stretches; banded leg curls for 3 sets of 12 reps.'
    ),
    # Injury: Shin Splints
    (
        'Shin Splints',
        'Pain along the inner edge of the shinbone caused by overuse, common in runners.',
        'Rest and ice; gradual return to activity with proper footwear; strengthening of calf muscles and improving running technique.',
        '3 sets of 15 reps of calf raises; foam rolling on the calves for 5 minutes.'
    ),
    # Injury: Achilles Tendinitis
    (
        'Achilles Tendinitis',
        'Inflammation of the Achilles tendon, typically due to overuse.',
        'Rest, ice, and anti-inflammatory measures; eccentric strengthening exercises for the calf muscles; gradual return to activity.',
        '3 sets of 12 reps of eccentric calf raises; banded ankle mobility exercises.'
    ),
    # Injury: Tennis Elbow (Lateral Epicondylitis)
    (
        'Tennis Elbow (Lateral Epicondylitis)',
        'Pain on the outer part of the elbow due to overuse of forearm muscles.',
        'Rest and avoid aggravating activities; forearm stretching and strengthening; use of a counterforce brace during activities.',
        '3 sets of 12 reps of wrist curls with a resistance band.'
    ),
    # Injury: Groin Pull
    (
        'Groin Pull',
        'Strain of the inner thigh muscles, common in sports requiring sudden changes in direction.',
        'Rest and ice; gentle stretching; progressive strengthening of the adductor muscles; avoid sudden movements during recovery.',
        '3 sets of 20 seconds per side of adductor stretches; banded hip abduction for 3 sets of 15 reps.'
    ),
    # Injury: Rotator Cuff Injury
    (
        'Rotator Cuff Injury',
        'Injury to the muscles and tendons that stabilize the shoulder joint.',
        'Rest and avoid overhead activities; shoulder strengthening and stabilization exercises; gradual return to sports.',
        '3 sets of 15 reps of external rotations with a resistance band.'
    ),
    # Injury: Runner’s Knee (Patellofemoral Pain Syndrome)
    (
        'Runner’s Knee (Patellofemoral Pain Syndrome)',
        'Pain around the kneecap, often associated with running or jumping activities.',
        'Rest and avoid activities that cause pain; strengthening of quadriceps and hip muscles; proper footwear and running technique.',
        '3 sets of 15 reps of quadriceps stretches; foam rolling for the IT band.'
    ),
    # Injury: Plantar Fasciitis
    (
        'Plantar Fasciitis',
        'Inflammation of the thick band of tissue that runs across the bottom of the foot.',
        'Rest and ice; stretching of the plantar fascia and calf muscles; use of supportive footwear; gradual return to activity.',
        '3 sets of 20-second plantar fascia stretches; banded ankle mobility exercises.'
    ),
    # Injury: ACL Tear
    (
        'ACL Tear',
        'Tear of the anterior cruciate ligament in the knee, often occurring during sudden stops or changes in direction.',
        'Surgical intervention may be required; post-surgery rehabilitation includes range-of-motion exercises, strengthening, and balance training.',
        '3 sets of 10 reps of knee extensions with a resistance band; hip mobility exercises.'
    ),
    # Injury: Concussion
    (
        'Concussion',
        'Mild traumatic brain injury caused by a blow to the head, common in contact sports.',
        'Immediate rest from physical and cognitive activities; gradual return to activity under medical supervision; monitoring for persistent symptoms.',
        'Gentle neck stretches; relaxation exercises for mental recovery.'
    ),
    # Disability: Lower Back Pain
    (
        'Lower Back Pain',
        'Pain or discomfort in the lower back, often caused by improper posture or overuse.',
        'Rest, heat therapy, and gentle stretching; strengthening of core muscles and maintaining proper posture.',
        '3 sets of 10 reps of pelvic tilts; bird-dog exercise for 3 sets of 12 reps.'
    ),
    # Disability: Arthritis (Knee)
    (
        'Arthritis (Knee)',
        'Degenerative condition affecting the knee joint, leading to pain, stiffness, and reduced mobility.',
        'Low-impact exercises like swimming; strengthening the quadriceps and hamstrings; stretching for flexibility.',
        '3 sets of 15 reps of leg raises; stationary cycling for 10 minutes.'
    ),
    # Disability: Sciatica
    (
        'Sciatica',
        'Pain radiating along the sciatic nerve, often caused by compression or irritation of nerve roots.',
        'Rest, ice, and anti-inflammatory medications; gentle stretching for the lower back and hamstrings.',
        '3 sets of 15-second hamstring stretches; lying on your back and pulling knees toward chest for 3 sets of 20 seconds.'
    ),
    # Disability: Carpal Tunnel Syndrome
    (
        'Carpal Tunnel Syndrome',
        'Compression of the median nerve in the wrist, causing numbness and tingling in the hand and fingers.',
        'Rest and ergonomic adjustments; wrist exercises and stretches.',
        '3 sets of 15 reps of wrist stretches; nerve gliding exercises for 3 sets of 10 reps.'
    ),
    # Disability: Stroke Recovery
    (
        'Stroke Recovery',
        'Recovery process following a stroke, which often involves muscle weakness, loss of motor control, and difficulty with balance.',
        'Physical therapy focusing on regaining motor skills and coordination; balance exercises.',
        'Standing on one leg for 30 seconds (3 sets each leg); arm lifts using light weights.'
    ),
    # Disability: Hip Replacement Recovery
    (
        'Hip Replacement Recovery',
        'Recovery from hip joint replacement surgery, which involves strengthening and regaining mobility in the hip region.',
        'Rehabilitation exercises, including strengthening of the hip and leg muscles; range-of-motion exercises.',
        '3 sets of 10 reps of leg lifts; seated marching exercises for 3 sets of 15 reps.'
    ),
    # Disability: Chronic Fatigue Syndrome
    (
        'Chronic Fatigue Syndrome',
        'A complex disorder characterized by persistent fatigue that doesn’t improve with rest.',
        'Gradual return to physical activity; energy conservation strategies; low-intensity aerobic exercises.',
        'Gentle stretching for 15 minutes; walking for 10 minutes at a low pace.'
    ),
    # Disability: Multiple Sclerosis
    (
        'Multiple Sclerosis',
        'An autoimmune condition that affects the central nervous system, leading to muscle weakness, coordination problems, and fatigue.',
        'Physical therapy for strengthening, balance exercises, and coordination training.',
        '3 sets of 10 reps of leg raises; balance exercises like standing on one leg for 30 seconds.'
    ),
    # Disability: Fibromyalgia
    (
        'Fibromyalgia',
        'A condition characterized by widespread muscle pain, fatigue, and tenderness in localized areas.',
        'Gentle exercise like swimming or walking; stretching and relaxation techniques.',
        'Gentle stretching for 20 minutes; walking for 10 minutes at a low pace.'
    ),
    # Disability: Spinal Cord Injury
    (
        'Spinal Cord Injury',
        'Injury to the spinal cord that results in loss of sensation or movement in parts of the body.',
        'Physical therapy for regaining strength and mobility; specialized exercises for coordination and function.',
        'Range-of-motion exercises for 10 minutes; seated leg lifts for 3 sets of 12 reps.'
    ),
    # Disability: Knee Osteoarthritis
    (
        'Knee Osteoarthritis',
        'Degeneration of the cartilage in the knee joint, leading to pain, swelling, and reduced movement.',
        'Low-impact exercises; strengthening of the quadriceps and hamstrings; knee protection strategies.',
        '3 sets of 15 reps of seated leg extensions; stationary cycling for 10 minutes.'
    )
]



cursor.executemany('''
INSERT INTO injuries (injury_name, description, training_plan, exercises)
VALUES (?, ?, ?, ?) 
''', injuries_data)


conn.commit()
conn.close()

print("Database and table created and data inserted successfully")