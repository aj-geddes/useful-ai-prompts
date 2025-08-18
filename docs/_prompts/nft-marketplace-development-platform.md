---
"category": |-
  blockchain
"compatible_models":
- |-
  GPT-4
- |-
  Claude 3
- |-
  Gemini Pro
"date": |-
  2025-01-14
"description": |-
  This prompt helps you build comprehensive NFT marketplaces with minting, trading, royalties, and creator tools for digital art, collectibles, and tokenized assets.
"layout": |-
  prompt
"prompt": |-
  -- Users table
  CREATE TABLE users (
      id UUID PRIMARY KEY,
      wallet_address VARCHAR(42) UNIQUE NOT NULL,
      username VARCHAR(50) UNIQUE,
      email VARCHAR(255),
      profile_image_url TEXT,
      verification_level INTEGER DEFAULT 0,
      created_at TIMESTAMP DEFAULT NOW()
  );

  -- NFT Collections
  CREATE TABLE collections (
      id UUID PRIMARY KEY,
      contract_address VARCHAR(42) NOT NULL,
      creator_id UUID REFERENCES users(id),
      name VARCHAR(255) NOT NULL,
      description TEXT,
      image_url TEXT,
      royalty_percentage DECIMAL(5,2),
      total_supply INTEGER,
      created_at TIMESTAMP DEFAULT NOW()
  );

  -- NFT Items
  CREATE TABLE nft_items (
      id UUID PRIMARY KEY,
      collection_id UUID REFERENCES collections(id),
      token_id INTEGER NOT NULL,
      name VARCHAR(255) NOT NULL,
      description TEXT,
      image_url TEXT NOT NULL,
      metadata_url TEXT,
      current_owner_id UUID REFERENCES users(id),
      creator_id UUID REFERENCES users(id),
      is_minted BOOLEAN DEFAULT FALSE,
      created_at TIMESTAMP DEFAULT NOW()
  );

  -- Marketplace Listings
  CREATE TABLE listings (
      id UUID PRIMARY KEY,
      nft_item_id UUID REFERENCES nft_items(id),
      seller_id UUID REFERENCES users(id),
      listing_type VARCHAR(20) NOT NULL, -- 'fixed', 'auction', 'offer'
      price DECIMAL(20,8) NOT NULL,
      currency VARCHAR(10) DEFAULT 'ETH',
      start_time TIMESTAMP DEFAULT NOW(),
      end_time TIMESTAMP,
      is_active BOOLEAN DEFAULT TRUE,
      created_at TIMESTAMP DEFAULT NOW()
  );
"related_prompts":
- |-
  smart-contract-security-audit-platform
- |-
  decentralized-finance-protocol-development
- |-
  blockchain-digital-identity-management-platform
"slug": |-
  nft-marketplace-development-platform
"tags":
- |-
  NFT marketplace
- |-
  digital collectibles
- |-
  art platform
- |-
  tokenization
- |-
  web3
"title": |-
  NFT Marketplace Builder
"use_cases":
- |-
  NFT marketplace development
- |-
  digital art platform
- |-
  collectibles trading
- |-
  creator monetization
"version": |-
  2.0.0
---
