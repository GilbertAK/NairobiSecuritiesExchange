import time
import os
import platform
from colorama import Fore, Style, init
from market_simulator import MarketSimulator
from ml_engine import NSEPredictor
from config import REFRESH_RATE

init(autoreset=True)

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def print_header():
    print(Fore.CYAN + Style.BRIGHT + "="*75) # Élargi à 75
    print(Fore.WHITE + Style.BRIGHT + "   🇰🇪 NAIROBI SECURITIES EXCHANGE - AI PREDICTIVE TERMINAL")
    print(Fore.CYAN + Style.BRIGHT + "="*75)
    # Alignement synchronisé avec les données ci-dessus
    print(f"{'SYMBOL':<10} | {'PRICE':<10} | {'CHG%':<10} | {'   AI PREDICTION (T+1)':<22} | {'TREND'}")
    print("-" * 75)

def main():
    market = MarketSimulator()
    predictor = NSEPredictor()
    
    try:
        while True:
            clear_screen()
            print_header()
            
            updates = market.update_market()
            
            for symbol, data in updates.items():
                price = data['price']
                change = data['pc_change']
                prediction = predictor.predict_next_price(data['history'])
                
                # Visual logic
                color = Fore.GREEN if change >= 0 else Fore.RED
                trend_icon = "▲" if prediction > price else "▼"
                trend_color = Fore.GREEN if prediction > price else Fore.RED
                
                # AJUSTEMENT ICI : Augmentation de l'espacement entre les colonnes
                print(f"{Fore.YELLOW + symbol:<10} | "           # Passé de <8 à <10
                      f"{Style.BRIGHT + str(f'{price:.2f}'):<10} | " 
                      f"{color + f'{change:+.2f}%':<10} | "      # Passé de <8 à <10
                      f"  {Style.DIM + f'KSh {prediction:.2f}':<20} | " # Ajout d'espaces avant KSh
                      f"{trend_color + trend_icon}")

            print("\n" + Fore.BLACK + Style.BRIGHT + f"Last Sync: {time.strftime('%H:%M:%S')} | Frequency: {REFRESH_RATE}s")
            print(Fore.CYAN + "Press Ctrl+C to exit trading session.")
            
            time.sleep(REFRESH_RATE)
            
    except KeyboardInterrupt:
        print(Fore.MAGENTA + "\n[INFO] Trading session closed by user.")

if __name__ == "__main__":
    main()


