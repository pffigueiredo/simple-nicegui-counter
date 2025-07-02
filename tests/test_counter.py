from nicegui.testing import User

async def test_counter_initial_state(user: User) -> None:
    """Test that counter starts at 0"""
    await user.open('/')
    
    # Check that counter starts at 0
    await user.should_see(marker='counter-display')
    await user.should_see('0')

async def test_counter_increment(user: User) -> None:
    """Test that clicking + button increments the counter"""
    await user.open('/')
    
    # Find and click the + button
    user.find(marker='increment-btn').click()
    
    # Check that counter increased to 1
    await user.should_see('1')

async def test_counter_decrement(user: User) -> None:
    """Test that clicking - button decrements the counter"""
    await user.open('/')
    
    # First increment to have a positive number
    user.find(marker='increment-btn').click()
    user.find(marker='increment-btn').click()  # Counter should be 2
    
    # Then decrement once
    user.find(marker='decrement-btn').click()  # Counter should be 1
    
    # Check the result
    await user.should_see('1')

async def test_counter_can_go_negative(user: User) -> None:
    """Test that counter can go below zero"""
    await user.open('/')
    
    # Click the - button to go negative
    user.find(marker='decrement-btn').click()
    
    # Check that counter is -1
    await user.should_see('-1')

async def test_counter_multiple_operations(user: User) -> None:
    """Test multiple increment and decrement operations"""
    await user.open('/')
    
    # Perform multiple operations: +3, -1, +2 = 4
    for _ in range(3):
        user.find(marker='increment-btn').click()
    user.find(marker='decrement-btn').click()
    for _ in range(2):
        user.find(marker='increment-btn').click()
    
    # Check final result
    await user.should_see('4')